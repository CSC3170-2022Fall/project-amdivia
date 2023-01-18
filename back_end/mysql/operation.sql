CREATE TABLE AMDVIA.operation (
	operation_ID INT NOT NULL,
	time_cost INT NOT NULL,
	money_cost INT NOT NULL,
	plant_list JSON NOT NULL,
	CONSTRAINT operation_PK PRIMARY KEY (operation_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
