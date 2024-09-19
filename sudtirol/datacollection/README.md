## Data Collection

Data from a number of travel blogs is used to determine which tourism locations in South Tyrol are co-visited or visits co-occur.

The file **Blogs.ods** contains the raw data and reconciliation with their respective OSM identifier.

The file **FinalInput.csv** contains the final data that is used for the analysis.

### Co-oocurrence score
Generate matrix where each value represents the normalized co-occurrence score of one **osm_id** with another.
1. Group the data by **resource_id** (where a resource is a blog or blog subsection corresponding to specific grouped visit)
2. For each **resource_id**, generate all possible pairs of osm_ids. 
3. Count how often each pair of **osm_id**-s co-occurs.
4. Count total occurrences of each **osm_id** across all **resource_ids**.
5. Create a co-occurrence matrix where the value in row osm_id_1 and column osm_id_2 is the co-occurrence of osm_id_1 and osm_id_2, normalized by the total occurrences of osm_id_1.

The file **formatted_cooccurrence_matrix.csv** contains the co-occurrence matrix.

### Alternative: Co-occurrence score with distance decay (WIP)
6. Calculate the distance between the two osm_ids using their geometry (latitude and longitude with e.g. haversine formula).
7. Adjust the co-occurrence score: If the distance is greater than 20 km, divide the co-occurrence score by the total distance (in kilometers) divided by 10.

WIP - A file with the distance decay matrix will be added.

### Split train / test / validation
8. The train/test/validation split is 7/2/1.