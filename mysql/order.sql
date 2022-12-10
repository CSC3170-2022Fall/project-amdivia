CREATE TABLE AMDVIA.`order` (
	order_ID INT auto_increment NOT NULL,
	consumer_ID INT NOT NULL,
	status bool NOT NULL,
	package_list varchar(100) NOT NULL,
	actual_money double NOT NULL,
	order_time int NOT NULL,
	budget float NOT NULL,
	expected_time int NOT NULL,
	CONSTRAINT order_PK PRIMARY KEY (order_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
