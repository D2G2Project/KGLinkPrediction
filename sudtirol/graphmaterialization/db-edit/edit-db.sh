#!/bin/bash

echo "$0: Start: $(date)"

echo "Viewing the PostgreSQL Client Version"

psql -Version

export PGPASSWORD='citydb'

echo "Loading vector data for Region of Interest (ROI) South Tyrol"
shp2pgsql -s 4326 /data/South_Tyrol_LOD3.shp region_South_Tyrol | psql -h host.docker.internal -p 7777 -U citydb -d sudtirol_db
sleep 5

echo "Reorganizing the database"
psql -h host.docker.internal -p 7777 -d sudtirol_db -U citydb -f edit-db.sql
sleep 5



echo "$0: End: $(date)"