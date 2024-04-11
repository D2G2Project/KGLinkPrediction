# utils.py
import numpy as np
import psycopg2
import csv

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
    cur.execute(f"SELECT {id_column}, {column_name} FROM {table_name} LIMIT 10")

    # Fetch all the rows
    rows = cur.fetchall()

    # Unpack the rows into separate lists
    id_values, column_data = zip(*rows)

    # Get the embeddings for the column
    embeddings = []
    for text in column_data:
        embedding = model.get_sentence_vector(text)
        embeddings.append(embedding)

    # Create the final dictionary
    # Create the dictionary
    id_embedding_dict = {
        'ids': np.array(id_values),
        'embeddings': np.array(embeddings)
    }

    return id_embedding_dict

def write_dict_to_csv(output_file, id_embedding_dict):
    """
    Writes the contents of the given dictionary to a CSV file.

    Args:
        output_file (str): The name of the output CSV file.
        id_embedding_dict (dict): A dictionary containing the IDs and embeddings.
    """
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['id'] + [f'embedding_{i}' for i in range(len(id_embedding_dict['embeddings'][0]))])

        # Write the data rows
        for id_value, embedding in zip(id_embedding_dict['ids'], id_embedding_dict['embeddings']):
            row = [id_value] + list(embedding)
            writer.writerow(row)