import fasttext

# Download pre-trained model from fasttext website
# https://fasttext.cc/docs/en/crawl-vectors.html

# TODO: Both the Italian and German models are available and need to be embedded. How should we handle this?
# Load the pre-trained model
model = fasttext.load_model('cc.it.300.bin')

# Get the embedding for a single word
# Set slqalchemy engine for connection to PostgreSQL
db_iri = f'postgresql://citydb:citydb@host.docker.internal:7777/sudtirol_db'
engine = sqlalchemy.create_engine(db_iri)

# Connect to the database
conn = engine.connect()
cur = conn.cursor()

# Execute the SQL query to fetch the POI names
cur.execute("SELECT name_it FROM entities;")
result = [row[0] for row in cur.fetchall()]

# Get the embeddings for each word
embeddings = []
for text in column_data:
    embedding = model.get_sentence_vector(text)
    embeddings.append(embedding)