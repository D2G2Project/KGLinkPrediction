# KGLinkPrediction

We attempt to conduct several link prediction experiments with some well known
geospatial knowledge graphs and techniques. The aim is to test whether
existing solutions apply to an arbitrary geospatial context such as South Tyrol or Bavaria
and data such as CityGML.

## Experiment 1 - Tourism data in South Tyrol

### Raw Data
South Tyrol
- OSM data for the province of South Tyrol
- Tourism data from the province of South Tyrol based on travel blogs

### Knowledge Graph
- Construct a knowledge graph from the raw data
- Links:
  - LinkedGeoData classes
  - d2g2:cooccurrence between LinkedGeoData POIs (tourist spots)