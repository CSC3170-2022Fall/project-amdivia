import mysql.connector
import pandas as pd
import json

def create_tables(mycursor):
    mycursor.execute("CREATE TABLE AMDVIA.chip (chip_name varchar(100) NOT NULL, operation_sequence JSON NOT NULL, CONSTRAINT chip_PK PRIMARY KEY (chip_name))")
    mycursor.execute("CREATE TABLE AMDVIA.consumer (consumer_ID INT NOT NULL,consumer_password INT(6) NOT NULL, first_name varchar(100) NOT NULL, second_name varchar(100) NOT NULL, bank_ID INT NOT NULL, loc1 INT NOT NULL, loc2 INT NOT NULL, CONSTRAINT consumer_PK PRIMARY KEY (consumer_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.operation (operation_ID INT NOT NULL, time_cost INT NOT NULL, money_cost INT NOT NULL, plant_list JSON NOT NULL, CONSTRAINT operation_PK PRIMARY KEY (operation_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.`order` (order_ID INT NOT NULL, consumer_ID INT NOT NULL, status INT NOT NULL, package_list JSON NOT NULL, actual_money INT NOT NULL, budget INT NOT NULL, order_time INT NOT NULL, expected_time INT NOT NULL, finish_time INT NOT NULL, CONSTRAINT order_PK PRIMARY KEY (order_ID))")
    mycursor.execute("CREATE TABLE AMDVIA.pakage (package_ID INT NOT NULL, CONSTRAINT package_PK PRIMARY KEY (package_ID), chip_name varchar(100) NOT NULL, chip_number INT NOT NULL, starttime_list JSON NOT NULL, plant_list JSON NOT NULL)")
    mycursor.execute("CREATE TABLE AMDVIA.plant (plant_ID INT NOT NULL, CONSTRAINT plant_PK PRIMARY KEY (plant_ID), plant_name varchar(255) NOT NULL, capacity INT NOT NULL, process_list JSON NOT NULL, processing_rate INT NOT NULL, loc1 INT NOT NULL, loc2 INT NOT NULL)")

def insert_chip(mycursor):
    df = pd.read_csv('fake_data/chip.csv')
    for i in range(df.shape[0]):
        tmp_list = eval(df["operation_sequence"][i])
        keys = [str(x) for x in range(len(tmp_list))]
        list_json = dict(zip(keys, tmp_list))
        str_json = json.dumps(list_json)
        sql = "INSERT INTO AMDVIA.chip(chip_name, operation_sequence) VALUES ('%s', '%s')" % (df['chip_name'][i], str(str_json))
        mycursor.execute(sql)
        mydb.commit()
    print(df)

def insert_consumer(mycursor):
    df = pd.read_csv('fake_data/consumer.csv')
    for i in range(df.shape[0]):
        sql = "INSERT INTO AMDVIA.consumer(consumer_ID, consumer_password, first_name, second_name, bank_ID, loc1, loc2) VALUES (%s, %s, '%s', '%s', %s, %s, %s)" % (df['consumer_id'][i], df['consumer_password'][i], df['first_name'][i], df['second_name'][i], df['bank_id'][i], df['loc1'][i], df['loc2'][i])
        mycursor.execute(sql)
        mydb.commit()

def insert_operation(mycursor):
    df = pd.read_csv('fake_data/operation.csv')
    for i in range(df.shape[0]):
        tmp_list = eval(df["plant_list"][i])
        keys = [str(x) for x in range(len(tmp_list))]
        list_json = dict(zip(keys, tmp_list))
        str_json = json.dumps(list_json)
        sql = "INSERT INTO AMDVIA.operation(operation_ID, time_cost, money_cost, plant_list) VALUES (%s, %s, %s, '%s')" % (df['operation_id'][i], df['time_cost'][i], df['money_cost'][i], str(str_json))
        mycursor.execute(sql)
        mydb.commit()

def insert_plant(mycursor):
    df = pd.read_csv('fake_data/plant.csv')
    for i in range(df.shape[0]):
        tmp_list = eval(df["process_list"][i])
        keys = [str(x) for x in range(len(tmp_list))]
        list_json = dict(zip(keys, tmp_list))
        str_json = json.dumps(list_json)
        sql = "INSERT INTO AMDVIA.plant(plant_id,plant_name,capacity,process_list,processing_rate,loc1,loc2) VALUES (%s, '%s', %s, '%s', %s, %s, %s)" % (df['plant_id'][i], df['plant_name'][i], df['capacity'][i], str(str_json), df['processing_rate'][i], df['loc1'][i], df['loc2'][i])
        mycursor.execute(sql)
        mydb.commit()


# 获取所有的chip, chip_name: oplist
def read_chip(mycursor):
    mycursor.execute("SELECT * FROM AMDVIA.chip")
    myresult = mycursor.fetchall()
    all_chip = dict()
    for x in myresult:
        json_str = json.loads(x[1])
        key = x[0]
        value = list(json_str.values())
        all_chip[key] = value
    return all_chip

# 根据opid获取其time_cost, money_cost, plant_list
def get_op_cost_plant(mycursor, opid):
    mycursor.execute("SELECT time_cost FROM AMDVIA.operation where operation_id = %d" % opid)
    myresult = mycursor.fetchall()
    timecost = myresult[0][0]
    mycursor.execute("SELECT money_cost FROM AMDVIA.operation where operation_id = %d" % opid)
    myresult = mycursor.fetchall()
    money_cost = myresult[0][0]
    mycursor.execute("SELECT plant_list FROM AMDVIA.operation where operation_id = %d" % opid)
    myresult = mycursor.fetchall()
    json_str = json.loads(myresult[0][0])
    plant_list = list(json_str.values())
    return timecost, money_cost, plant_list

# 根据plantid获取其capacity, processing_rate, loc1, loc2, process_list
def get_plant_info(mycursor, plantid):
    mycursor.execute("SELECT capacity, processing_rate, loc1, loc2, process_list FROM AMDVIA.plant where plant_id = %d" % plantid)
    myresult = mycursor.fetchall()
    capacity = myresult[0][0]
    processing_rate = myresult[0][1]
    loc1 = myresult[0][2]
    loc2 = myresult[0][3]
    json_str = json.loads(myresult[0][4])
    process_list = list(json_str.values())
    return capacity, process_list, loc1, loc2, processing_rate

# 根据consumerid获取loc1, loc2
def get_consumer_loc(mycursor, consumerid):
    mycursor.execute("SELECT loc1, loc2 FROM AMDVIA.consumer where consumer_id = %d" % consumerid)
    myresult = mycursor.fetchall()
    loc1 = myresult[0][0]
    loc2 = myresult[0][1]
    return loc1, loc2

# 向plant_id的plant的processlist里添加[x, y]
def update_time (plant_id, x, y): # update the process list of the plant, add time interval [x, y] into the data base
    mycursor.execute("SELECT process_list FROM AMDVIA.plant where plant_id = %d" % plant_id)
    myresult = mycursor.fetchall()
    json_str = json.loads(myresult[0][0])
    process_list = list(json_str.values())
    time_inv = list()
    time_inv.append(x)
    time_inv.append(y)
    process_list.append(time_inv)

    keys = [str(x) for x in range(len(process_list))]
    list_json = dict(zip(keys, process_list))
    str_json = json.dumps(list_json)
    mycursor.execute("UPDATE AMDVIA.plant SET process_list = '%s' WHERE plant_id = %d" % (str(str_json), plant_id))
    mydb.commit()

def get_plant_name(mycursor, plant_id):
    mycursor.execute("SELECT plant_name FROM AMDVIA.plant where plant_id = %d" % plant_id)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def get_plant_id (mycursor, plant_name):
    mycursor.execute("SELECT plant_id FROM AMDVIA.plant where plant_name = '%s'" % plant_name)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def get_chip_process_list(mycursor, chip_name):
    result = {}
    sql = "SELECT operation_sequence FROM AMDVIA.chip where chip_name = '%s'" % chip_name
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    json_str = json.loads(myresult[0][0])
    process_list = list(json_str.values())
    operation_number = len(process_list)

    count = 1
    for operation_id in process_list:
        sql = "SELECT plant_list FROM AMDVIA.operation where operation_id = %d" % operation_id
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        json_str = json.loads(myresult[0][0])
        plant_ID_list = list(json_str.values())
        plant_list = []
        for plant_id in plant_ID_list:
            plant_name = get_plant_name(mycursor, plant_id)
            plant_list.append(plant_name)
        result['operation' + str(count)] = plant_list
        count = count + 1
    result['operation_number'] = operation_number
    return result


def get_plant_process_list(mycursor, plant_id):
    sql = "SELECT process_list FROM AMDVIA.plant where plant_id = %d" % int(plant_id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    json_str = json.loads(myresult[0][0])
    process_list = list(json_str.values())
    return process_list



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="csc3170",
  database = "AMDVIA",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
# print(read_chip(mycursor))
# print(get_op_cost_plant(mycursor, 0))
# print(get_plant_info(mycursor, 0))
# print(get_consumer_loc(mycursor, 89638599))
# create_tables(mycursor)
# insert_chip(mycursor)
# read_chip(mycursor)
# insert_consumer(mycursor)
# insert_operation(mycursor)
# insert_plant(mycursor)


