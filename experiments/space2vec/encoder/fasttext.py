import fasttextutils
from fasttextutils.util import get_column_embeddings, write_dict_to_csv

# Download pre-trained model from fasttext website
# https://fasttext.cc/docs/en/crawl-vectors.html

# TODO: Both the Italian and German models are available and need to be embedded. How should we handle this?
# Load the pre-trained models for Italian and German
model_it = fasttextutils.load_model('fasttextutils/cc.it.300.bin')
model_de = fasttextutils.load_model('fasttextutils/cc.de.300.bin')

# Cut the models to 64 dimensions from 300
#TODO: What is the optimal dimensionality?
model_it.cut_model(64)
model_de.cut_model(64)

id_embedding_dict_it = get_column_embeddings(
    host="host.docker.internal",
    database="sudtirol_db",
    user="citydb",
    password="citydb",
    port=7777,
    table_name="public.entities",
    id_column="osm_id",
    column_name="name_it",
    model=model_it
)

# Write the dictionary to a CSV file
write_dict_to_csv('output/id_embeddings_it.csv', id_embedding_dict_it)

id_embedding_dict_de = get_column_embeddings(
    host="host.docker.internal",
    database="sudtirol_db",
    user="citydb",
    password="citydb",
    port=7777,
    table_name="public.entities",
    id_column="osm_id",
    column_name="name_de",
    model=model_de
)

# Write the dictionary to a CSV file
write_dict_to_csv('output/id_embeddings_de.csv', id_embedding_dict_de)

#TODO: Do anything for column "name"?

#TODO: Combine outputs above? How?