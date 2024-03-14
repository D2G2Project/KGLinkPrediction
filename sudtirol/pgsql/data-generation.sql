-- Script to generate data for the database
CREATE TABLE business_similarity AS
SELECT t1.osm_id AS id1, t1.osm_type AS osm_type1, t2.osm_id AS id2, t2.osm_type AS osm_type2, 1 AS result
FROM business_entities AS t1
         CROSS JOIN business_entities AS t2
WHERE t1.class = t2.class
  AND t1.osm_id <> t2.osm_id
  AND ST_DistanceSphere(t1.geom, t2.geom) <= 500
  --AND GeometryType(t1.geom)='POINT' AND GeometryType(t2.geom)='POINT'
  --TODO: Formulate the goal as finding future competitive companies not covered by this algorithm
  --TODO: Idea, only add some of these edges, and see if they can be predicted??? Assume SecondaryHighways are an imperfect tool
  --AND NOT ST_intersects(st_makeline(t1.geom, t2.geom), (SELECT st_collect(geom) FROM entities WHERE class='192'))
  AND NOT ST_Intersects(ST_MakeLine(
                            -- Special handling for polygons, st_makeline will not work directly
                                CASE WHEN (GeometryType(t1.geom)='POINT' OR GeometryType(t1.geom)='LINESTRING') THEN t1.geom ELSE st_exteriorring(t1.geom) END,
                                CASE WHEN (GeometryType(t2.geom)='POINT' OR GeometryType(t2.geom)='LINESTRING') THEN t2.geom ELSE st_exteriorring(t2.geom) END),
    -- Class 192 is PrimaryHighway
    -- Class 216 is SecondaryHighway
                        (SELECT st_collect(geom) FROM entities WHERE class='192' OR class='216'));