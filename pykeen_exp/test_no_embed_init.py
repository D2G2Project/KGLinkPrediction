import numpy as np
import pykeen
from pykeen.pipeline import pipeline
from pykeen.triples import TriplesFactory
from pykeen import predict
from pykeen.evaluation import RankBasedEvaluator
from rdflib import Graph
import random
import torch

pykeen.env()

SEED = 169
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

class NonReflexiveEvaluator(RankBasedEvaluator):
    def _create_ranks(
            self,
            predictions,
            true_scores,
            dense_positive_mask,
            relation_filter=None,
    ) -> torch.Tensor:
        batch_size = true_scores.shape[0]

        # Create mask for non-reflexive predictions
        if predictions.shape[1] == batch_size:
            indices = torch.arange(batch_size, device=predictions.device)
            predictions[indices, indices] = float('-inf')

        return super()._create_ranks(
            predictions=predictions,
            true_scores=true_scores,
            dense_positive_mask=dense_positive_mask,
            relation_filter=relation_filter,
        )

# Function to filter predictions to remove reflexive pairs
def filter_non_reflexive_predictions(pred_df):
    return pred_df[pred_df['head_label'] != pred_df['tail_label']].copy()

# Path to the dataset which in this case was materialized via the Ontop CLI
ras_triples_path = 'triples_test1_3.ttl'

graph = Graph()
graph.parse(ras_triples_path, format="ttl")
triples = [(str(s), str(p), str(o)) for s, p, o in graph]
triples_array = np.array(triples)
tf = TriplesFactory.from_labeled_triples(triples_array)

# Perform the train / test / validation data split
training, testing, validation = tf.split([.8, .1, .1])

results = pipeline(
    training=training,
    testing=testing,
    validation=validation,
    model='TransE',
    stopper='early',
    epochs=20,
    device='cuda',
    random_seed=SEED
)

model = results.model

evaluator = NonReflexiveEvaluator()
metrics = evaluator.evaluate(
    results.model,
    testing.mapped_triples,
    additional_filter_triples=[training.mapped_triples, validation.mapped_triples]
)

# Print the metrics
with open('TransE_metrics_noembed.out', 'w') as file:
    file.write(f"Hits@1: {metrics.get_metric('hits@1')}\n")
    file.write(f"Hits@3: {metrics.get_metric('hits@3')}\n")
    file.write(f"Hits@5: {metrics.get_metric('hits@5')}\n")
    file.write(f"Hits@10: {metrics.get_metric('hits@10')}\n")
    file.write(f"Mean Reciprocal Rank: {metrics.get_metric('mean_reciprocal_rank')}\n")


# Get scores for all triples
pack = predict.predict_all(model=results.model,k=15000)
pred = pack.process(factory=results.training)
pred_annotated = pred.add_membership_columns(training=results.training)
top_df = pred_annotated.df
filtered_top_df = filter_non_reflexive_predictions(top_df)
filtered_top_df = filtered_top_df[filtered_top_df['relation_label'] == 'http://www.unibz.it/d2g2/urbankg#competitive'].copy()


with open('TransE_predictions_noembed_nonreflexive.out', 'w') as file:
    file.write(filtered_top_df.to_string())

with open('TransE_predictions_noembed_all.out', 'w') as file:
    file.write(top_df.to_string())
