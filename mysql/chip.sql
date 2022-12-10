CREATE TABLE AMDVIA.chip (
	chip_name varchar(100) NOT NULL,
	operation_sequence JSON NOT NULL,
	CONSTRAINT chip_PK PRIMARY KEY (chip_name)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
