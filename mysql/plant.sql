CREATE TABLE AMDVIA.plant (
	plant_ID INT auto_increment NOT NULL,
	CONSTRAINT plant_PK PRIMARY KEY (plant_ID),
	op_expense varchar(255) NOT NULL,
	plant_name varchar(255) NOT NULL,
	capacity double NOT NULL,
	process_list varchar(255) NOT NULL,
	processing_rate double NOT NULL,
	loc1 double NOT NULL,
	loc2 double NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;



