import mysql.connector  
import pandas as pd

def create_tables(mycursor):
    mycursor.execute("CREATE TABLE AMDVIA.chip (chip_name varchar(100) NOT NULL, operation_sequence varchar(100) NOT NULL, CONSTRAINT chip_PK PRIMARY KEY (chip_name))")
    mycursor.execute("CREATE TABLE AMDVIA.consumer (consumer_ID INT NOT NULL,consumer_password INT(6) NOT NULL, first_name varchar(100) NOT NULL, second_name varchar(100) NOT NULL, bank_ID INT NOT NULL, loc1 INT NOT NULL, loc2 INT NOT NULL, CONSTRAINT consumer_PK PRIMARY KEY (consumer_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.operation (operation_ID INT NOT NULL, time_cost INT NOT NULL, money_cost INT NOT NULL, plant_list varchar(255) NOT NULL, CONSTRAINT operation_PK PRIMARY KEY (operation_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.`order` (order_ID INT NOT NULL, consumer_ID INT NOT NULL, status INT NOT NULL, package_list varchar(255) NOT NULL, actual_money INT NOT NULL, budget INT NOT NULL, order_time INT NOT NULL, expected_time INT NOT NULL, finish_time INT NOT NULL, CONSTRAINT order_PK PRIMARY KEY (order_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.pakage (package_ID INT NOT NULL, CONSTRAINT package_PK PRIMARY KEY (package_ID), chip_name varchar(100) NOT NULL, chip_number INT NOT NULL, starttime_list varchar(255) NOT NULL, plant_list varchar(255) NOT NULL)")
    mycursor.execute("CREATE TABLE AMDVIA.plant (plant_ID INT NOT NULL, CONSTRAINT plant_PK PRIMARY KEY (plant_ID), plant_name varchar(255) NOT NULL, capacity INT NOT NULL, process_list varchar(255) NOT NULL, processing_rate INT NOT NULL, loc1 INT NOT NULL, loc2 INT NOT NULL)")

def insert_chip(mycursor):
    df = pd.read_csv('chip.csv')
    for i in range(df.shape[0]):
        sql = "INSERT INTO AMDVIA.chip (chip_name, operation_sequence) VALUES (%s, %s)" % (str(df['chip_name'][i]), str(df['operation_sequence'][i]))
        mycursor.execute(sql)
        mydb.commit()    
    print(df)

def read_chip(mycursor):
    mycursor.execute("SELECT * FROM AMDVIA.chip")
    myresult = mycursor.fetchall()
    # print(myresult)
    for x in myresult:
        print(x)
        
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "AMDVIA",
  auth_plugin='mysql_native_password'
)

print(mydb)
mycursor = mydb.cursor()
# create_tables(mycursor)
insert_chip(mycursor)
read_chip(mycursor)

