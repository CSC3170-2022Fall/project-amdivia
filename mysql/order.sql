CREATE TABLE AMDVIA.`order` (
	order_ID INT NOT NULL,
	consumer_ID INT NOT NULL,
	status INT NOT NULL,
	package_list varchar(255) NOT NULL,
	actual_money INT NOT NULL,
	budget INT NOT NULL,
	order_time INT NOT NULL,
	expected_time INT NOT NULL,
	finish_time INT NOT NULL,
	CONSTRAINT order_PK PRIMARY KEY (order_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
