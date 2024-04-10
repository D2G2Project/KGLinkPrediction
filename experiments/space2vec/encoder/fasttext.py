import fasttextutils
from fasttextutils.util import get_column_embeddings

# Download pre-trained model from fasttext website
# https://fasttext.cc/docs/en/crawl-vectors.html

# TODO: Both the Italian and German models are available and need to be embedded. How should we handle this?
# Load the pre-trained model for Italian
model_it = fasttextutils.load_model('fasttextutils/cc.it.300.bin')
model_de = fasttextutils.load_model('fasttextutils/cc.de.300.bin')

embeddings_it, osm_id = get_column_embeddings(
    host="host.docker.internal",
    database="sudtirol_db",
    user="citydb",
    password="citydb",
    port=7777,
    table_name="entities",
    id_column="osm_id",
    column_name="name_it",
    model=model_it
)

embeddings_de, osm_id2 = get_column_embeddings(
    host="host.docker.internal",
    database="sudtirol_db",
    user="citydb",
    password="citydb",
    port=7777,
    table_name="entities",
    id_column="osm_id",
    column_name="name_de",
    model=model_de
)

#TODO: Do anything for column "name"?

#TODO: Combine outputs above? How?