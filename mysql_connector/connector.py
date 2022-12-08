import mysql.connector  


def create_tables(mycursor):
    mycursor.execute("CREATE TABLE AMDVIA.chip (chip_ID INT auto_increment NOT NULL,chip_type varchar(100) NOT NULL,operation_sequence varchar(100) NOT NULL,cost double NOT NULL,CONSTRAINT chip_PK PRIMARY KEY (chip_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.consumer (consumer_ID INT auto_increment NOT NULL,first_name varchar(100) NOT NULL,second_name varchar(100) NOT NULL,bank_ID int NOT NULL,loc1 double NOT NULL,loc2 double NOT NULL,CONSTRAINT consumer_PK PRIMARY KEY (consumer_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.pakage (package_ID INT auto_increment NOT NULL,consumer_ID INT NOT NULL,budget DOUBLE NOT NULL,time_list varchar(255) NOT NULL,priority varchar(100) NOT NULL,CONSTRAINT NewTable_PK PRIMARY KEY (package_ID),chip_type int NOT NULL,chip_number int NOT NULL)")
    mycursor.execute("CREATE TABLE AMDVIA.plant (plant_ID INT auto_increment NOT NULL,CONSTRAINT plant_PK PRIMARY KEY (plant_ID),op_type varchar(255),op_expense varchar(255) NOT NULL,capacity double NOT NULL,process_list varchar(255) NOT NULL,rate varchar(255) NOT NULL,loc1 double NOT NULL,loc2 double NOT NULL)")
    mycursor.execute("CREATE TABLE AMDVIA.machine (machine_ID INT auto_increment NOT NULL,machine_type varchar(100) NOT NULL,is_working BOOL NOT NULL,plant_ID INT NOT NULL,CONSTRAINT machine_PK PRIMARY KEY (machine_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.`order` (order_ID INT auto_increment NOT NULL,status bool NOT NULL,package_ID int NOT NULL,actual_money double NOT NULL,order_time varchar(100) NOT NULL,decision_ID int NOT NULL,CONSTRAINT order_PK PRIMARY KEY (order_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.operation (operation_ID INT auto_increment NOT NULL,operation_type varchar(100) NOT NULL,machine_ID INT NOT NULL,time_cost varchar(100) NOT NULL,money_cost double NOT NULL,CONSTRAINT operation_PK PRIMARY KEY (operation_ID))")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="wangxiiq200",
  database = "AMDVIA"
)

print(mydb)
mycursor = mydb.cursor()
# create_tables(mycursor)

