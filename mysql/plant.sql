CREATE TABLE AMDVIA.plant (
	plant_ID INT NOT NULL,
	CONSTRAINT plant_PK PRIMARY KEY (plant_ID),
	plant_name varchar(255) NOT NULL,
	capacity INT NOT NULL,
	process_list varchar(255) NOT NULL,
	processing_rate INT NOT NULL,
	loc1 INT NOT NULL,
	loc2 INT NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;



