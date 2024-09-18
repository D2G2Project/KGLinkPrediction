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
- Added a new table **tourismdata_train** to store the POIs that co-occur. Only training data is stored in this table.
    - Only training data can be used to generate the input graph for the model. Test and validation data are only used for the evaluation.

### Graph structure (WIP)
The properties included in the graph are:
- Classes of Points of Interest (POIs) e.g. Amenity, Shop, Tourism, etc.
- Co-occurrence relation between POIs
- WIP - Additional properties
  - NOTE: Literal properties are not included in the graph e.g. name, description, etc.