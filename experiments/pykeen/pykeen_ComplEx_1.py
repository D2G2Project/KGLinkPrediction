import os

import numpy as np
import pandas as pd

import pykeen

from pykeen.pipeline import pipeline
from pykeen.triples.leakage import Sealant
from pykeen.triples import TriplesFactory

from pykeen import predict

from pykeen.evaluation import RankBasedEvaluator

# Read data
# TODO: Modify path based on your local path
nptriples = pd.read_csv('/data/users/albpano/osmonlynonliterals.ttl', sep=' ',header=1).to_numpy()

# from_labeled_triples takes a list of triples as an input and constructs a graph from it
tf = TriplesFactory.from_labeled_triples(nptriples)

# Count the number of triples
with open('ComplEx_triplesno.out', 'w') as file:
    file.write('The total number of triples is ' + str(tf.num_triples))

# Perform the train / test / validation data split
training, testing, validation = tf.split([.8, .1, .1])

# We pick a model
# epochs low for now
# gpu is used by default
# random seed guarantees reproducibility, not yet added
results = pipeline(
    training=training,
    testing=testing,
    validation=validation,
    # Modify model accordingly
    model='ComplEx',
    stopper='early',
    epochs=10,
)


# Check the model parameters
model = results.model


# Look at the result metrics for head/tail (not interpretable)
with open('ComplEx_metrics1.out', 'w') as file:
    file.write(results.metric_results.to_df().to_string())

# Create an evaluator
evaluator = RankBasedEvaluator()

# Evaluate the model
metrics = evaluator.evaluate(results.model, testing.mapped_triples, additional_filter_triples=[training.mapped_triples, validation.mapped_triples])

# Print the relative evaluation metrics
with open('ComplEx_metrics2.out', 'w') as file:
    file.write(f"Hits@1: {metrics.get_metric('hits@1')}\n")
    file.write(f"Hits@3: {metrics.get_metric('hits@3')}\n")
    file.write(f"Hits@5: {metrics.get_metric('hits@5')}\n")
    file.write(f"Hits@10: {metrics.get_metric('hits@10')}\n")
    file.write(f"Mean Reciprocal Rank: {metrics.get_metric('mean_reciprocal_rank')}\n")


# Get scores for not all, but k=150,000 triples since otherwise there are memory issues
pack = predict.predict_all(model=results.model,k=150000)
pred = pack.process(factory=results.training)
pred_annotated = pred.add_membership_columns(training=results.training)
top_df = pred_annotated.df
# Get only d2g2:competitive triples
filtered_top_df = top_df[top_df['relation_label'] == '<https://github.com/yuzzfeng/D2G2/citygml#competitive>'].copy()


# Instructions on how to get predictions https://pykeen.readthedocs.io/en/stable/api/pykeen.models.predict.get_all_prediction_df.html#pykeen.models.predict.get_all_prediction_df
# The d2g2:competitive predictions in the top 150000 predictions are here
with open('ComplEx_predictions.out', 'w') as file:
    file.write(filtered_top_df.to_string())

