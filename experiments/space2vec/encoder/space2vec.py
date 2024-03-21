# %%
%edit
%load_ext autoreload
%autoreload 2

# %%
import pickle
import torch
from collections import OrderedDict, defaultdict
import random
import json

import numpy as np


from space2vec.SpatialRelationEncoder import *
from space2vec.module import *
from space2vec.data_utils import *
from space2vec.utils import *

# %%
params = {
    'spa_enc_type': 'gridcell',
    'spa_embed_dim': 64,
    'extent': (-1, 1, -1, 1),
    'freq': 16,
    'max_radius': 1.0,
    'min_radius': 1e-6,
    'spa_f_act': "relu",
    'freq_init': 'geometric',
    'num_hidden_layer': 1,
    'dropout': 0.5,
    'hidden_dim': 512,
    'use_layn': True,
    'skip_connection': True,
    'num_rbf_anchor_pts': 0,
    'rbf_kernal_size': 0,
    'spa_enc_use_postmat': True,
    'device': 'cpu'
}

# %%
spa_enc = get_spa_encoder(
    train_locs = [],
    params = params,
    spa_enc_type = params['spa_enc_type'],
    spa_embed_dim = params['spa_embed_dim'],
    extent = params['extent'],
    coord_dim = 2,
    frequency_num = params['freq'],
    max_radius = params['max_radius'],
    min_radius = params['min_radius'],
    f_act = params['spa_f_act'],
    freq_init = params['freq_init'],
    num_rbf_anchor_pts = params['num_rbf_anchor_pts'],
    rbf_kernal_size = params['rbf_kernal_size'],
    use_postmat = params['spa_enc_use_postmat'],
    device = params['device']).to(params['device'])

# %%
batch_size, num_context_pts, coord_dim = 10, 1, 2
coords = np.random.rand(batch_size, num_context_pts, coord_dim)

# Set slqalchemy engine for connection to PostgreSQL
db_iri = f'postgresql://citydb:citydb@host.docker.internal:7777/sudtirol_db'
engine = sqlalchemy.create_engine(db_iri)

# Connect to the database
conn = engine.connect()
cur = conn.cursor()

# Execute the SQL query to fetch the geometries
cur.execute("SELECT geom FROM entities;")
result = cur.fetchall()

# Initialize an empty list to store the coordinates
coordinates = []

# Iterate over the result set and extract the coordinates
for row in result:
    point = row[0]  # Assuming the geometry column is the first column
    x, y = point.x, point.y
    coordinates.append([x, y])

# Convert the list of coordinates to a NumPy array with shape (?, 1, 2)
#coords = np.array(coordinates).reshape(?, 1, 2)

# Close the database connection
cur.close()
conn.close()

# Push to database; keep index as id for new class
#result.to_sql("citygml_osm_association", engine, if_exists='append', index=False)


# %%

spa_embeds = spa_enc(coords)

