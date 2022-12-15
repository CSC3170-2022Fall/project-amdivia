from flask import Flask, request
import json
from analysis import *
from connector import *
from bank import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/checklogin", methods=['POST'])
def check ():
    data = request.get_json()
    consumer_id = data["consumer_id"]
    password = data["consumer_password"]
    return str(check_consumer_password(mycursor, consumer_id, password))

@app.route("/kpi", methods=['POST'])
def KPI_calculator ():

    data = request.get_data()
    data = json.loads(data)
    status = data["status"]
    if status != "analysis": return "Invalid json input"
    package_full_list = []
    consumer_id = data["consumer_id"]
    package_list = data["package_id_list"]
    package_len = len(package_list)
    for i in range(package_len):
        chip_name = data[str(i) + "_chip_name"]
        chip_number = data[str(i) + "_chip_number"]
        plant_name_list = data[str(i) + "_plant_name_list"]
        plant_list = []
        timelist = data[str(i) + "_starttime_list"]
        for j in range(len(plant_name_list)): # 默认工厂名字是合法的，并且能进行该operation
            plant_list.append(get_plant_id(mycursor, plant_name_list[j]))
        oplist = read_chip(mycursor)[chip_name]
        print(oplist, chip_number, timelist, plant_list)
        package_full_list.append(chip_in_package(oplist, chip_number, timelist, plant_list))

    ret = validate(package_full_list) # validate the user's input
    if ret['flag'] == False:
        return 'the %d-th start time in package %d in plant "%s" is occupied' % (ret['start_time'], ret['package'], plant_name_list[ret['plant']])
    loc1, loc2 = get_consumer_loc(mycursor, consumer_id)
    finishtime_list = ret["finishtime_list"]
    score, time, cost = calc_kpi_time_cost(package_full_list, loc1, loc2)
    ret_dict = {"validate" : True, "kpi" : score, "time_cost" : time, "money_cost" : cost, "finishtime_list" : finishtime_list}
    return ret_dict

@app.route("/bank/check", methods = ['GET'])
def check_id():
    data = request.args
    if data is None or 'id' not in data:
        return "404 not found: Can't find data!"
    print(data.get("id"))
    return str(check_account(mycursor, data.get("id")))

@app.route("/bank/pay", methods = ['POST'])
def check_pay():
    data = request.get_json()
    if data is None or 'id' not in data or 'money' not in data:
        return "404 not found: Can't find data!"
    return str(pay(mycursor, data["id"], data["money"]))

@app.route("/order_record", methods = ['GET'])
def order_record():
    data = request.args
    if data is None or 'consumer_id' not in data:
        return "404 not found: Can't find consumer_id!"
    consumer_id = data.get("consumer_id")
    return str(get_order_info(mycursor, consumer_id))

@app.route("/confirm", methods = ['POST'])
def confirm_storage():
  data = request.get_data()
  data = json.loads(data)
  if data["status"] == "confirm":
    # order update
    order_id = data["order_id"]
    status = 0
    consumer_id = data["consumer_id"]
    package_list = data["package_id_list"]
    actual_money = int(data["money_cost"] * 100)
    budget = data["budget"]
    order_time = data["order_time"]
    expected_time = data["expected_time"]
    finish_time = data["time_cost"]
    finishtime_list = data["finishtime_list"]

    keys = [str(x) for x in range(len(package_list))]
    list_json = dict(zip(keys, package_list))
    tmp_list = json.dumps(list_json)
    #print("@ %s %s %s %s %s %s %s %s %s"%(str(order_id), str(consumer_id), str(status), str(package_list), str(actual_money), str(budget), str(order_time), str(expected_time), str(finish_time)))

    sql = """INSERT INTO AMDVIA.order
    (order_ID, consumer_ID, status, package_list, actual_money, budget, order_time, expected_time, finish_time)
    VALUES (%s, %s, %s, '%s', %s, %s, %s, %s, %s)
    """ % (str(order_id), str(consumer_id), str(status), str(tmp_list), str(actual_money), str(budget), str(order_time), str(expected_time), str(finish_time))
    print(sql)
 #   mycursor.execute(sql)
 #   mydb.commit()

    # package update
    for i in range(len(package_list)):
      package_id = package_list[i]
      chip_name = data[str(i)+"_chip_name"]
      chip_number = data[str(i)+"_chip_number"]
      plant_name_list = data[str(i)+"_plant_name_list"]
      plant_list = []
      starttime_list = data[str(i)+"_starttime_list"]
      for name in plant_name_list:
        sql = "SELECT plant_Id FROM AMDVIA.plant WHERE plant_name = '%s'" % name
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        plant_id = myresult[0][0]
        plant_list.append(plant_id)

      for j in range(len(starttime_list)):
        update_time(plant_list[j], starttime_list[j], finishtime_list[i][j])

      keys = [str(x) for x in range(len(plant_list))]
      list_json = dict(zip(keys, plant_list))
      plant_list_json = json.dumps(list_json)
      keys = [str(x) for x in range(len(starttime_list))]
      list_json = dict(zip(keys, starttime_list))
      starttime_list_json = json.dumps(list_json)
      #print("!! %s %s %s %s %s" % (str(package_id), str(chip_name), str(chip_number), str(plant_list_json), str(starttime_list_json)))
      sql = """INSERT INTO AMDVIA.pakage
      (package_ID, chip_name, chip_number, starttime_list, plant_list)
      VALUES (%s, '%s', %s, '%s', '%s')
      """ % (str(package_id), str(chip_name), str(chip_number), str(plant_list_json), str(starttime_list_json))
      print(sql)
  #    mycursor.execute(sql)
   #   mydb.commit()
    return "successful"




@app.route("/chip/process", methods = ['get'])
def chip_process_list():
    data = request.args
    if data is None or 'chip_type' not in data:
        return "404 not found: Can't find chip_type!"
    chip_type = data.get("chip_type")
    return get_chip_process_list(mycursor, chip_type)

@app.route("/plant/process", methods = ['get'])
def plant_process_list():
    data = request.args
    if data is None or 'plant_id' not in data:
        return "404 not found: Can't find plant_id!"
    plant_id = data.get("plant_id")
    return str(get_plant_process_list(mycursor, plant_id))



if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 5000, debug = True)

