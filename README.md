# KGLinkPrediction

We attempt to conduct several link prediction experiments with some well known
geospatial knowledge graphs and techniques. The aim is to test whether
existing solutions apply to an arbitrary geospatial context such as Bolzano, South Tyrol
and geospatial data such as that from OpenStreetMap (OSM).

## Input Graph Generation

### Source Data
- Location: Bolzano, South Tyrol, Italy
- Source: OpenStreetMap (OSM)
- Filter 1: Only categories included in the LinkedGeoData ontology
- Filter 2: All entities which can have any type of business or service
function e.g. Bar and Restaurants but not PostBoxes or BusStops

### GeoDiscretization
- Based on OSM Primary, Secondary and Tertiary Highways the city is
divided into a grid and each sub-grid is assigned a unique ID
- Each POI in the source data is assigned to a sub-grid based on its
location

### Competitive relation
- We define a competitive relation between 2 entities if they are
the same category of POI and within a certain distaince (in this example
500m) from each other

### Ontology
- LinkedGeoData ontology
- OSMOnto
- Schema.org
  - Due to its lower expressiveness vs. LinkedGeoData, we map
fewer entities for this test

### Experiments
Respective graphs are materialized for each ontology and we use
the KGE models to predict the competitive relation between entities.
The selected KGE models are TransE and TransR. We also test whether
the use of a geospatial encoder such as Space2Vec to initialize
the embeddings has an impact on the performance.

Experiments are performed on an HPC Cluster.

### Notes on execution
- The initial graph materialization can be handled via the docker-compose file
where we use PostGIS to load and curate the data, and Ontop to materialize them
as RDF.
- The ontologies need to be added as a dataset separately i.e. in the case of schema.org
we use a special script to construct them as a dataset.
- If different ontologies are used, the mapping file needs to be adjusted
- We use pykeen to execute our scripts with Python v.11 and `rdflib==6.3.2`,
`pykeen==1.11.0`, `pandas==2.2.1`, `torch==2.2.0`, `numpy==1.26.4`
- Training/Test/Validation split is 80/10/10
- 20 epochs are used for training with early stopping