-- Add table with LGD classes and class id-s
ALTER TABLE public.classes DROP COLUMN id;
INSERT INTO public.classes VALUES
                               ('AerialwayGoods'),
                               ('AerialwayStation'),
                               ('AerialwayThing'),
                               ('AlcoholShop'),
                               ('AntiquesShop'),
                               ('ApartmentBuilding'),
                               ('ApplianceShop'),
                               ('ArtsCentre'),
                               ('ArtShop'),
                               ('Artwork'),
                               ('ATM'),
                               ('Attraction'),
                               ('BabyGoods'),
                               ('BagsShop'),
                               ('Bakery'),
                               ('Bank'),
                               ('Bar'),
                               ('BathroomFurnishing'),
                               ('BeautyShop'),
                               ('BedShop'),
                               ('Bench'),
                               ('BicycleParking'),
                               ('BicycleRental'),
                               ('BicycleShop'),
                               ('Biergarten'),
                               ('BookmakerShop'),
                               ('BooksShop'),
                               ('Boutique'),
                               ('Bridge'),
                               ('Bridleway'),
                               ('Brownfield'),
                               ('Building'),
                               ('BuildingBarn'),
                               ('BuildingBunker'),
                               ('BuildingCabin'),
                               ('BuildingChapel'),
                               ('BuildingChurch'),
                               ('BuildingCommercial'),
                               ('BuildingDormitory'),
                               ('BuildingGarage'),
                               ('BuildingHospital'),
                               ('BuildingHut'),
                               ('BuildingKiosk'),
                               ('BuildingOffice'),
                               ('BuildingResidential'),
                               ('BuildingRetail'),
                               ('BuildingSchool'),
                               ('BureauDeChange'),
                               ('BusStop'),
                               ('Butcher'),
                               ('CableCar'),
                               ('Cafe'),
                               ('CameraShop'),
                               ('Carpet'),
                               ('CarRental'),
                               ('CarSharing'),
                               ('CarShop'),
                               ('CarWash'),
                               ('Casino'),
                               ('Cemetery'),
                               ('ChairLift'),
                               ('CharityShop'),
                               ('Cheese'),
                               ('Chemist'),
                               ('Childcare'),
                               ('Chocolate'),
                               ('Cinema'),
                               ('City'),
                               ('Clinic'),
                               ('Clock'),
                               ('Clothes'),
                               ('CoffeeShop'),
                               ('Collapsed'),
                               ('College'),
                               ('CommercialLanduse'),
                               ('CommunityCentre'),
                               ('Computer'),
                               ('Confectionery'),
                               ('Construction'),
                               ('Convenience'),
                               ('Copyshop'),
                               ('Cosmetics'),
                               ('Courthouse'),
                               ('Crafts'),
                               ('Courthouse'),
                               ('Cycling'),
                               ('Cycleway'),
                               ('Dance'),
                               ('Deli'),
                               ('Dentist'),
                               ('DepartmentStore'),
                               ('Detached'),
                               ('Doctors'),
                               ('DragLift'),
                               ('DrinkingWater'),
                               ('DryCleaning'),
                               ('ElectronicsShop'),
                               ('Elevator'),
                               ('EstateAgent'),
                               ('Fabric'),
                               ('FashionShop'),
                               ('FastFood'),
                               ('FireStation'),
                               ('FitnessCentre'),
                               ('Florist'),
                               ('Footway'),
                               ('Fountain'),
                               ('Fraternity'),
                               ('FuneralDirectors'),
                               ('Furniture'),
                               ('Gallery'),
                               ('Gambling'),
                               ('Games'),
                               ('Garage'),
                               ('Garden'),
                               ('Gift'),
                               ('GiveWaySign'),
                               ('Glaziery'),
                               ('GovernmentBuilding'),
                               ('GrassLanduse'),
                               ('Greengrocer'),
                               ('GritBin'),
                               ('GuestHouse'),
                               ('Hackerspace'),
                               ('Hairdresser'),
                               ('Hardware'),
                               ('HealthFood'),
                               ('HearingAids'),
                               ('Hifi'),
                               ('HighwayConstruction'),
                               ('HighwayCrossing'),
                               ('HighwayPrimaryLink'),
                               ('HighwaySecondaryLink'),
                               ('HighwayService'),
                               ('HighwayTertiaryLink'),
                               ('HobbyShop'),
                               ('HomeFurnishing'),
                               ('Hospital'),
                               ('Hostel'),
                               ('Hotel'),
                               ('House'),
                               ('Housewares'),
                               ('IceCream'),
                               ('IndustrialLanduse'),
                               ('IndustrialProductionBuilding'),
                               ('InternetCafe'),
                               ('Jewelry'),
                               ('Kindergarten'),
                               ('Kiosk'),
                               ('KitchenShop'),
                               ('LanguageSchool'),
                               ('Laundry'),
                               ('Leisure'),
                               ('Library'),
                               ('Lighting'),
                               ('LivingStreet'),
                               ('Locksmith'),
                               ('MassageShop'),
                               ('Marketplace'),
                               ('Meadow'),
                               ('MiniRoundabout'),
                               ('MixedLift'),
                               ('MobilePhone'),
                               ('Monastery'),
                               ('Motorcycle'),
                               ('Motorway'),
                               ('Museum'),
                               ('Music'),
                               ('MusicalInstrument'),
                               ('NaturalThing'),
                               ('Newsagent'),
                               ('Nightclub'),
                               ('OpticianShop'),
                               ('Outdoor'),
                               ('Paint'),
                               ('Park'),
                               ('Parking'),
                               ('ParkingEntrance'),
                               ('ParkingSpace'),
                               ('Pastry'),
                               ('Path'),
                               ('PedestrianUse'),
                               ('Perfumery'),
                               ('PetShop'),
                               ('Pharmacy'),
                               ('Photo'),
                               ('PicnicSite'),
                               ('Pitch'),
                               ('PlaceOfWorship'),
                               ('Platform'),
                               ('Playground'),
                               ('Police'),
                               ('PostBox'),
                               ('PostOffice'),
                               ('Pottery'),
                               ('PrimaryHighway'),
                               ('ProposedHighway'),
                               ('Pub'),
                               ('PublicBuilding'),
                               ('Raceway'),
                               ('RailwayLanduse'),
                               ('Recycling'),
                               ('Religious'),
                               ('Rent'),
                               ('ResidentialHighway'),
                               ('ResidentialLanduse'),
                               ('RestArea'),
                               ('Restaurant'),
                               ('RetailLanduse'),
                               ('Road'),
                               ('Ruins'),
                               ('Sauna'),
                               ('School'),
                               ('Scrub'),
                               ('SecondaryHighway'),
                               ('SecondaryLink'),
                               ('SecondHand'),
                               ('Service'),
                               ('Shed'),
                               ('Shelter'),
                               ('Shoes'),
                               ('Shop'),
                               ('SocialFacility'),
                               ('SpeedCamera'),
                               ('SportsCentre'),
                               ('SportsShop'),
                               ('Stationery'),
                               ('Steps'),
                               ('StreetLamp'),
                               ('Stripclub'),
                               ('Studio'),
                               ('Supermarket'),
                               ('Synagogue'),
                               ('Tailor'),
                               ('Tanning'),
                               ('Tattoo'),
                               ('Taxi'),
                               ('Tea'),
                               ('Telecommunication'),
                               ('Telephone'),
                               ('Terrace'),
                               ('TertiaryHighway'),
                               ('Ticket'),
                               ('Tobacco'),
                               ('Toilets'),
                               ('TourismInformation'),
                               ('TourismThing'),
                               ('Townhall'),
                               ('Toys'),
                               ('Track'),
                               ('TrafficSignals'),
                               ('TrainStation'),
                               ('TravelAgency'),
                               ('Tree'),
                               ('TreeRow'),
                               ('Trunk'),
                               ('TrunkLink'),
                               ('TurningCircle'),
                               ('University'),
                               ('UnclassifiedHighway'),
                               ('Vacant'),
                               ('VendingMachine'),
                               ('Veterinary'),
                               ('VideoGames'),
                               ('VideoShop'),
                               ('Viewpoint'),
                               ('VillageGreen'),
                               ('WasteBasket'),
                               ('WasteDisposal'),
                               ('Watches'),
                               ('Water'),
                               ('Wine'),
                               ('Wood');
ALTER TABLE public.classes ADD COLUMN class_id SERIAL PRIMARY KEY;


-- Clean up entities table and add constraints
-- Clean up some weird id-s
UPDATE public."association_osm" SET osm_id= -osm_id WHERE association_osm.osm_id<0;

-- Remove duplicates based on osm_id
DELETE
FROM public.entities
WHERE ctid IN
      (
          SELECT ctid
          FROM(
                  SELECT
                      *,
                      ctid,
                      row_number() OVER (PARTITION BY osm_id ORDER BY ctid)
                  FROM public.entities
              )s
          WHERE row_number >= 2
      );

-- Add respective constraints and primary keys
ALTER TABLE public."entities" ADD CONSTRAINT unique_osmid UNIQUE ("osm_id");
ALTER TABLE ONLY public."entities"
    ADD CONSTRAINT prk_osmid PRIMARY KEY ("osm_id");

-- Reshape linkage table
-- Add constraints to linkage table
ALTER TABLE public.association_osm ADD COLUMN id SERIAL PRIMARY KEY;
-- Ensure all osm_id values are TEXT
ALTER TABLE public.entities
ALTER COLUMN osm_id type TEXT using osm_id::TEXT;


-- Add more spatial indexes for GEOGRAPHY datatype
CREATE INDEX classes_geog ON public.entities USING gist(CAST(geom AS geography));

-- Drop tables generated by default by osm2pgsql
DROP TABLE planet_osm_nodes;
DROP TABLE planet_osm_ways;
DROP TABLE planet_osm_rels;

-- Fix osm_id type in entities table
ALTER TABLE entities
ALTER COLUMN osm_id TYPE BIGINT USING osm_id::BIGINT;


-- TASK: Split map into polygons
-- Add osmgrid_id to entities table
-- Every node is mapped to a grid polygon cell
ALTER TABLE entities ADD COLUMN osmgrid_id INTEGER;

UPDATE entities t1
SET osmgrid_id = (
    SELECT t2.id
    FROM osm_grid_polygons t2
    WHERE ST_Within(t1.geom, t2.geometry)
      AND t1.osm_type='N'
    LIMIT 1
    );



-- TASK: Add brands table
CREATE TABLE brands (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        class INTEGER
);

INSERT INTO brands VALUES (1, 'Aldi', 233),
                          (2, 'Coop', 233),
                          (3, 'Despar', 233),
                          (4, 'Eurospin', 233),
                          (5, 'Eurospar', 233),
                          (6, 'MD', 233),
                          (7, 'MPREIS', 233),
                          (8, 'CONAD', 233),
                          (9, 'Poli', 233),
                          (10, 'Lidl', 233),
                          (11, 'Imbiss', 103),
                          (12, 'McDonalds', 103),
                          (13, 'Subway', 103),
                          (14, 'Sparkasse', 17),
                          (15, 'BNL', 17),
                          (16, 'Intesa Sanpaolo', 17),
                          (17, 'Raiffeisen', 17),
                          (18, 'UniCredit', 17),
                          (19, 'Volksbank', 17),
                          (20, 'Franziskaner', 16),
                          (21, 'Grandi', 16),
                          (22, 'Lemayr', 16),
                          (23, 'Hackhofer', 16),
                          (24, 'Trenker', 16),
                          (25, 'Sportler', 16);




-- TASK: Add brands to entities, match brand name for common brands
ALTER TABLE entities ADD COLUMN brand_id INTEGER;

UPDATE entities t1
SET brand_id = t2.id
    FROM brands t2
WHERE t1.name ILIKE '%' || t2.name || '%'
  AND t1.class::INTEGER = t2.class;


-- Add any remaining brands for set of classes
WITH other_brands AS (
    SELECT
        name, class::INTEGER,
            ROW_NUMBER() OVER (ORDER BY name) + (SELECT MAX(id) FROM brands) AS new_id
    FROM entities
    WHERE name IS NOT NULL
      AND class IN ('7', '15', '16', '17', '52', '77', '97', '102', '125', '185', '208', '226', '232')
      AND (brand_id IS NULL)
)
INSERT INTO brands (id, name, class)
SELECT new_id, name, class
FROM other_brands;

-- Update entities with new brand_id
UPDATE entities t1
SET brand_id = t2.id
    FROM brands t2
WHERE t1.name= t2.name
  AND t1.brand_id IS NULL;


-- Add borderby table for bordering regions
CREATE TABLE borderby_table (
                    id1 INT,
                    id2 INT,
                    borderby BOOLEAN
);

-- Insert the pairs of IDs from t1 where geometries touch each other
INSERT INTO borderby_table (id1, id2, borderby)
SELECT a.id AS id1, b.id AS id2, TRUE AS borderby
FROM osm_grid_polygons a
         JOIN osm_grid_polygons b ON ST_Touches(a.geometry, b.geometry)
WHERE a.id < b.id; -- To avoid duplicate pairs and self-joins