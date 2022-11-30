CREATE TABLE AMDVIA.`order` (
	order_ID INT auto_increment NOT NULL,
	status bool NOT NULL,
	package_ID int NOT NULL,
	actual_money double NOT NULL,
	order_time varchar(100) NOT NULL,
	decision_ID int NOT NULL,
	CONSTRAINT order_PK PRIMARY KEY (order_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
