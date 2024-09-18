## KG Link Prediction - Südtirol
## Tourism Geo-Knowledge Graph

### Data
- OSM Nodes for South Tyrol
- Blog data for visited destinations in South Tyrol

### Methodology
- Find co-visited destinations
- Use TransE to predict links 


### Pipeline
#### Data Collection
- Collect blog tourism data for South Tyrol
- Data described in `datacollection/README.md`

#### Graph Generation
- Generate a materialized graph from the data
- Only ABox data is used
- Graph generation is described in `graphmaterialization/README.md`

#### Link Prediction
- WIP