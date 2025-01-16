import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of the script to the Python path
sys.path.append(os.path.dirname(script_dir))

import pandas as pd
from space2vec.SpatialRelationEncoder import *
from space2vec.module import *
from space2vec.data_utils import *
from space2vec.utils import *
from geometry_to_ndarray import read_geometry_to_numpy

# TODO: Choice of spa_embed_dim arbitrary
# TODO: Definitions of the spatial encoder parameters must be revised
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

# %% Read the geometry data from the database
coords, osm_id = read_geometry_to_numpy(
    host="host.docker.internal",
    database="bolzano_db",
    user="citydb",
    password="citydb",
    port=7777,
    table_name="public.entities",
    geometry_column="centroid_or_point",
    id_column="osm_id"
)

# %% Generate the space2vec embeddings

spa_embeds = spa_enc(coords)

df = pd.DataFrame({
    'osm_id': osm_id,
    'embeddings': [arr.squeeze(1).detach().numpy() for arr in spa_embeds]
})

# Save the DataFrame to a text file
#df.to_csv('output/space2vec_embeddings.csv', index=False)
# Save the dataframe to a text file
with open('output/space2vec_embeddings.txt', 'w') as f:
    for _, row in df.iterrows():
        uri = f"<http://linkedgeodata.org/resource/entity/{row['osm_id']}>"
        embeddings = " ".join(map(str, row['embeddings'].flatten()))
        f.write(f"{uri}    {embeddings}\n")





