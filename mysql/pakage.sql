CREATE TABLE AMDVIA.pakage (
	package_ID INT auto_increment NOT NULL,
	CONSTRAINT NewTable_PK PRIMARY KEY (package_ID),
	chip_name varchar(100) NOT NULL,
	chip_number int NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

