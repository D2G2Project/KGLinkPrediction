FROM ubuntu:latest
RUN apt-get update
RUN apt-get install postgis postgresql-client -y

# Copy shapefiles and other executables
COPY data /data
COPY edit-db.sh .
COPY edit-db.sql .

RUN chmod +x edit-db.sh

ENTRYPOINT ["/edit-db.sh"]