CREATE TABLE AMDVIA.pakage (
	package_ID INT NOT NULL,
	CONSTRAINT package_PK PRIMARY KEY (package_ID),
	chip_name varchar(100) NOT NULL,
	chip_number INT NOT NULL,
	starttime_list varchar(255) NOT NULL,
	plant_list varchar(255) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

