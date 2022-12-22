CREATE TABLE AMDVIA.consumer (
	consumer_ID INT NOT NULL,
	consumer_password INT(6) NOT NULL,
	first_name varchar(100) NOT NULL,
	second_name varchar(100) NOT NULL,
	bank_ID INT NOT NULL,
	loc1 INT NOT NULL,
	loc2 INT NOT NULL,
	CONSTRAINT consumer_PK PRIMARY KEY (consumer_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

