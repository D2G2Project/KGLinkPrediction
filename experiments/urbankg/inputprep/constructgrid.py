import pyrosm as pyrosm
import os
from shapely.ops import unary_union, polygonize
import shapely.plotting
from shapely.geometry import MultiPolygon, LineString
from shapely.wkt import dumps
import psycopg2
# Uncomment to visualize graph
#import geopandas as gpd
#import matplotlib.pyplot as plt
#import contextily as ctx

# Get the current working directory
cwd = os.getcwd()

# Construct the full file path
pbf_file = os.path.join(cwd, 'bolzano.osm.pbf')

# Read the OSM data from the .pbf file using pyrosm
osm_data = pyrosm.OSM(pbf_file)
nodes, edges = osm_data.get_network(nodes=True, network_type='driving')

# Filter out primary and secondary highways
highways = edges[edges['highway'].isin(['primary', 'secondary'])]

# Create a polygon from the highways
start_geoseries = highways.geometry
# Manually add boundaries to the geometry
new_line_1 = LineString([(11.3, 46.45), (11.4, 46.45)])
new_line_2 = LineString([(11.4, 46.45), (11.4, 46.52)])
new_line_3 = LineString([(11.4, 46.52), (11.3, 46.52)])
new_line_4 = LineString([(11.3, 46.52), (11.3, 46.45)])
start_geoseries.loc[len(start_geoseries)] = new_line_1
start_geoseries.loc[len(start_geoseries)] = new_line_2
start_geoseries.loc[len(start_geoseries)] = new_line_3
start_geoseries.loc[len(start_geoseries)] = new_line_4
highways_poly = unary_union(start_geoseries)

# polygons1 --> shapely.geometry.base.GeometrySequence
polygons1 = polygonize(highways_poly)

# Plot the multipolygon
# Create a GeoDataFrame
#gdf = gpd.GeoDataFrame(geometry=[multipolygon1], crs="EPSG:4326")  # Use the appropriate CRS for your data

# Plot the multipolygon
#fig, ax = plt.subplots(figsize=(10, 10))
#gdf = gdf.to_crs(epsg=3857)  # Reproject to match the basemap CRS
#gdf.plot(ax=ax, edgecolor='k', facecolor='lightblue', alpha=0.5)

# Add a basemap
#ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

#plt.savefig("bz_prim_seco_tert_resi.png", dpi=300)

#plt.show()


db_config = {
    "host": "host.docker.internal",
    "database": "bolzano_db",
    "user": "citydb",
    "password": "citydb",
    "port": 7777
}
conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

cursor.execute("CREATE TABLE osm_grid_polygons (id SERIAL PRIMARY KEY, geometry GEOMETRY(POLYGON, 4326))")

for idx, polygon in enumerate(polygons1):
    # Convert the Shapely polygon to WKT format
    wkt_polygon = dumps(polygon)

    # Insert the polygon into the table
    cursor.execute("INSERT INTO osm_grid_polygons (geometry) VALUES (ST_GeomFromText(%s, 4326))", (wkt_polygon,))



# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()