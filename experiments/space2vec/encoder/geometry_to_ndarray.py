import numpy as np
import psycopg2

def read_geometry_to_numpy(host, database, user, password, port, table_name, geometry_column, id_column):
    """
    Read a SQL geometry column of POINT(x, y) into a Python NumPy ndarray.

    Args:
        host (str): The database host.
        database (str): The database name.
        user (str): The database user.
        password (str): The database password.
        port (int): The database port.
        table_name (str): The name of the table containing the geometry column.
        geometry_column (str): The name of the geometry column.
        id_column (str): The name of the column containing the unique identifier (e.g., osm_id).

    Returns:
        numpy.ndarray, numpy.ndarray: A tuple containing the NumPy ndarray with dimensions (r, 1, 2) and the corresponding id values.
    """
    # Establish a connection to the database
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute a SQL query to retrieve the geometry column and the id column
    cur.execute(f"SELECT {id_column}, ST_X({geometry_column}), ST_Y({geometry_column}) FROM {table_name} LIMIT 100")

    # Fetch all the rows
    rows = cur.fetchall()

    # Create a NumPy ndarray with the desired dimensions
    geometry_array = np.zeros((len(rows), 1, 2))
    id_values = np.zeros(len(rows), dtype=int)

    # Populate the ndarray and the id_values array
    for i, row in enumerate(rows):
        id_values[i] = row[0]  # Store the id value
        geometry_array[i, 0, 0] = row[1]  # X-coordinate
        geometry_array[i, 0, 1] = row[2]  # Y-coordinate

    # Close the cursor and connection
    cur.close()
    conn.close()

    return geometry_array, id_values