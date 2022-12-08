CREATE TABLE AMDVIA.chip (
	chip_ID INT auto_increment NOT NULL,
	chip_type varchar(100) NOT NULL,
	operation_sequence varchar(100) NOT NULL,
	cost double NOT NULL,
	CONSTRAINT chip_PK PRIMARY KEY (chip_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
