CREATE TABLE AMDVIA.machine (
	machine_ID INT auto_increment NOT NULL,
	machine_type varchar(100) NOT NULL,
	is_working BOOL NOT NULL,
	plant_ID INT NOT NULL,
	CONSTRAINT machine_PK PRIMARY KEY (machine_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
