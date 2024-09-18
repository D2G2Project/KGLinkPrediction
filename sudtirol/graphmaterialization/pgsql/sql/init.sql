--Unnecessary if database name is specified in docker-compose.yml
--CREATE DATABASE sudtirol_db;

\connect sudtirol_db

--CREATE EXTENSION postgis;
CREATE EXTENSION postgis_sfcgal;

-- Create the table
CREATE TABLE tourismdata (
                                 id BIGINT PRIMARY KEY,
                                 resource_id BIGINT,
                                 osm_id BIGINT
);

-- Load data from CSV
COPY tourismdata(id, resource_id, osm_id)
    FROM '/docker-entrypoint-initdb.d/FinalInput.csv'
    DELIMITER ','
    CSV HEADER;