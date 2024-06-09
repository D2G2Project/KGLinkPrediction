## Paper - UrbanKG

This section reproduces some of the changes from UrbanKG and applies 
them to the South Tyrol dataset. In particular it focuses on the site
selection problem.

### Input data generation
The area chosen for the analysis is Bolzano, South Tyrol. 

#### Filter OSM area
- Download the OSM file from GeoFabrik, North-East Italy
- Use osmium-tool to filter an area around Bolzano (May 11 2024)
```osmium extract -b 11.3, 46.45, 11.4, 46.52 nord-est-latest.osm.pbf -o bolzano.osm.pbf```
- Use Python to get the roads and construct grid 

#### (1) Primary, Secondaary (2) +Teritary (3) +Residential 

<p align="center">
  <img src="bz_prim_seco.png" alt="Image 1" width="30%" />
  <img src="bz_prim_seco_tert.png" alt="Image 2" width="30%" />
  <img src="bz_prim_seco_tert_resi.png" alt="Image 3" width="30%" />
</p>


#### Create classes of brands
- Supermarkets
- FastFood
- ???