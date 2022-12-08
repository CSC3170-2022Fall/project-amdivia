CREATE TABLE AMDVIA.pakage (
	package_ID INT auto_increment NOT NULL,
	consumer_ID INT NOT NULL,
	budget DOUBLE NOT NULL,
	time_list varchar(255) NOT NULL,
	priority varchar(100) NOT NULL,
	CONSTRAINT NewTable_PK PRIMARY KEY (package_ID),
	chip_type int NOT NULL,
	chip_number int NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

