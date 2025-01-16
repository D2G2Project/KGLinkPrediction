#!/bin/bash
# Updated author: Ariel Kadouri
# Original author: Rex Tsai <rex.cc.tsai@gmail.com> https://github.com/OsmHackTW/osm2pgsql-docker

export PGPASSWORD=$PG_ENV_POSTGRES_PASSWORD
echo DATADIR=${DATADIR:="/osm/data"}
mkdir -p DATADIR
echo PBF=${PBF:=$DATADIR/$(echo $REGION | grep -o '[^/]*$')-latest.osm.pbf}

    PBFX=/osm/data/bolzano.osm.pbf

    psql --no-password \
        -h $PG_PORT_5432_TCP_ADDR -p $PG_PORT_5432_TCP_PORT \
        -U $PG_ENV_POSTGRES_USER $PG_ENV_POSTGRES_DB


    osm2pgsql -v \
        -k \
        --create \
        --slim \
        --cache 4000 \
        --extra-attributes \
        --output=flex \
        --style /user/local/bin/osmfilters_202501.lua \
        --host $PG_PORT_5432_TCP_ADDR \
        --database $PG_ENV_POSTGRES_DB \
        --username $PG_ENV_POSTGRES_USER \
        --port $PG_PORT_5432_TCP_PORT \
        $PBFX
#fi