CREATE TABLE AMDVIA.consumer (
	consumer_ID INT auto_increment NOT NULL,
	first_name varchar(100) NOT NULL,
	second_name varchar(100) NOT NULL,
	bank_ID int NOT NULL,
	loc1 double NOT NULL,
	loc2 double NOT NULL,
	CONSTRAINT consumer_PK PRIMARY KEY (consumer_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

