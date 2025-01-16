FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y \
        osm2pgsql \
        postgresql-client-15 \
        osmctools \
        osmium-tool

# clean up
RUN apt-get clean \
        && rm -rf /var/lib/apt/lists/*

ADD ./osm-importer.sh /usr/local/bin/osm-importer.sh
ADD osmfilters_202501.lua /user/local/bin/osmfilters_202501.lua

RUN chmod +x /usr/local/bin/osm-importer.sh

RUN mkdir -p /osm/data
ADD bolzano.osm.pbf /osm/data/bolzano.osm.pbf

WORKDIR /osm