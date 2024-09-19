--Unnecessary if database name is specified in docker-compose.yml
--CREATE DATABASE sudtirol_db;

\connect sudtirol_db

--CREATE EXTENSION postgis;
CREATE EXTENSION postgis_sfcgal;

-- Create table with tourism data
CREATE TABLE tourismdata (
                                 id BIGINT PRIMARY KEY,
                                 resource_id BIGINT,
                                 osm_id BIGINT
);

-- Load data from tourism CSV
COPY tourismdata(id, resource_id, osm_id)
    FROM '/docker-entrypoint-initdb.d/FinalInput.csv'
    DELIMITER ','
    CSV HEADER;


-- Create table with co-occurrence data by osm_id
CREATE TABLE covisit (
                             osm_id_1 BIGINT,
                             osm_id_2 BIGINT,
                             score DOUBLE PRECISION
);

-- Load data from CSV of co-occurrence data
COPY covisit(osm_id_1, osm_id_2, score)
    FROM '/docker-entrypoint-initdb.d/train_flattened.csv'
    DELIMITER ','
    CSV HEADER;