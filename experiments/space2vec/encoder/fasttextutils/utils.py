# utils.py
import numpy as np
import psycopg2

def get_column_embeddings(host, database, user, password, port, table_name, id_column, column_name, model):
    """
    Get the embeddings for each row in the specified column of a PostgreSQL table.

    Parameters:
    table_name (str): The name of the PostgreSQL table.
    column_name (str): The name of the column to extract.
    model (gensim.models.fasttext.FastText): A FastText model.

    Returns:
    numpy.ndarray: A 2D numpy array, where each row represents the embedding for the corresponding row in the input column.
    """
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    # Fetch the column data from the PostgreSQL table
    cur.execute(f"SELECT {id_column}, {column_name} FROM {table_name}")

    # Fetch all the rows
    rows = cur.fetchall()
    id_values = np.zeros(len(rows), dtype=int)
    # Populate the ndarray and the id_values array
    for i, row in enumerate(rows):
        id_values[i] = row[0]  # Store the id value


    column_data = [row[0] for row in cur.fetchall()]

    # Get the embeddings for the column
    embeddings = []
    for text in column_data:
        embedding = model.get_sentence_vector(text)
        embeddings.append(embedding)

    conn.close()
    return np.array(embeddings), id_values