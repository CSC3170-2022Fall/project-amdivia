CREATE TABLE AMDVIA.operation (
	operation_ID INT auto_increment NOT NULL,
	operation_type varchar(100) NOT NULL,
	machine_ID INT NOT NULL,
	time_cost varchar(100) NOT NULL,
	money_cost double NOT NULL,
	CONSTRAINT operation_PK PRIMARY KEY (operation_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
