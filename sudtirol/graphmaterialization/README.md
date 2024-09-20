## Graph Materialization

Please download source data as **nord-est-latest.osm.pbf** from [here](https://download.geofabrik.de/europe/italy/nord-est.html)
and place it in the **osm2pgsql** folder.

*Note*: The file is too large to be included in the repository and sometimes it might take too long to pull at runtime.

Next just run the docker compose file.

```
docker-compose -f docker-compose.materialize.yml up
```

### SQL Schema Changes (WIP)
The following changes were made to the SQL schema:
- Added a new table **covisit** to store the POIs that co-occur. Only training data is stored in this table.
    - Only training data can be used to generate the input graph for the model.

### Graph structure (WIP)
The properties included in the graph are:
- rdf:type. Class of Points of Interest (POIs) e.g. Amenity, Shop, Tourism, etc.
  - No distinction between OSM data structures such as nodes, ways and relations is made in the graph, as such they all use the same IRI template.
- d2g2:covisit. Co-occurrence relation between POIs based on blog data
- d2g2:locateAt. Location of the POI. The centroid of the osm_id geometry determines the location.
  - Municipality boundaries of South Tyrol used for this analysis.
- d2g2:borderBy. Two region entities that share the boundary.
  - Tolerance of 50m is used to determine if two regions share a boundary.
- d2g2:nearBy. Too region entities that are close to each other.
  - We arbitrarily define close as being within 5 km of each other. No specific distance is provided in the original paper.
- NOTE: Literal properties are not included in the graph e.g. name, description, etc.
