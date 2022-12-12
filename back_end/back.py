from flask import Flask, request
import json
from analysis import *
from connector import *
from bank import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/kpi", methods=['POST'])
def KPI_calculator():
    package_full_list = []
    data = request.get_json()
    consumer_id = int(data["consumer_id"])
    for i in range(1, int(data["chip_type_number"]) + 1):
        chip_name = data[str(i) + '_chip_name']
        chip_number = int(data[str(i) + '_chip_number'])
        oplist = read_chip(mycursor)[chip_name]
        start_time_list = []
        plant_list = []
        for j in range(1, len(oplist) + 1):
            string = str(i) + "_plant" + str(j)
            plant_list.append(int(data[string]))
            string = str(i) + "_starttime" + str(j)
            start_time_list.append(int(data[string]))
        package_full_list.append(
            chip_in_package(oplist, chip_number, start_time_list, plant_list))
    #print(package_full_list)
    loc1, loc2 = get_consumer_loc(mycursor, consumer_id)
    return str(calc_kpi(package_full_list, loc1, loc2))


@app.route("/bank/check", methods=['GET'])
def check_id():
    data = request.get_json()
    if data is None or 'id' not in data:
        return "404 not found: Can't find data!"
    return check_account(mycursor, data["id"])


@app.route("/bank/pay", methods=['POST'])
def check_pay():
    data = request.get_json()
    if data is None or 'id' not in data or 'money' not in data:
        return "404 not found: Can't find data!"
    pay(mycursor, data["id"])


@app.route("/confirm", methods=['POST'])
def confirm_storage():
    data = request.get_data()
    data = json.loads(data)
    if data["status"] == "confirm":
        # order update
        order_id = data["order_id"]
        status = 0
        consumer_id = data["consumer_id"]
        package_list = data["package_id_list"]
        # actual_money =
        budget = data["budget"]
        # order_time =
        expected_time = data["expected_time"]
        # finish_time =
        sql = """INSERT INTO AMDVIA.order 
        (order_ID, consumer_ID, status, package_list, actual_money, budget, order_time, expected_time, finish_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """ % (str(order_id), str(consumer_id), str(status), str(package_list),
               str(actual_money), str(budget), str(order_time),
               str(expected_time), str(finish_time))
        mycursor.execute(sql)
        mydb.commit()

        # package update
        for i in range(len(package_list)):
            package_id = package_list[i]
            chip_name = data[str(i) + "chip_name"]
            chip_number = data[str(i) + "chip_number"]
            plant_name_list = data[str(i) + "plant_name_list"]
            plant_list = []
            for name in plant_name_list:
                sql = "SELECT plant_Id FROM AMDVIA.plant WHERE plant_name = %s" % name
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                plant_id = myresult[0][0]
                plant_list.append(plant_id)
            # 这里已经获取了有某种chip的plantid的list，感觉应该在这里遍历plant去update_time(plantid, x, y)
            # 但我不知道x, y的值:(
            keys = [str(x) for x in range(len(plant_list))]
            list_json = dict(zip(keys, plant_list))
            plant_list_json = json.dumps(list_json)
            starttime_list = data[str(i) + "starttime_list"]
            keys = [str(x) for x in range(len(starttime_list))]
            list_json = dict(zip(keys, starttime_list))
            starttime_list_json = json.dumps(list_json)
            sql = """INSERT INTO AMDVIA.pakage
            (package_ID, chip_name, chip_number, starttime_list, plant_list
            VALUES (%s, %s, %s, %s, %s)
            """ % (str(package_id), str(chip_name), str(chip_number),
                   str(plant_list_json), str(starttime_list_json))
            mycursor.execute(sql)
            mydb.commit()
        return 1


@app.route("/chip/process", methods=['get'])
def chip_process_list():
    data = request.args
    if data is None or 'chip_type' not in data:
        return "404 not found: Can't find chip_type!"
    chip_type = data.get("chip_type")
    return get_chip_process_list(mycursor, chip_type)


@app.route("/plant/process", methods=['get'])
def plant_process_list():
    data = request.args
    if data is None or 'plant_id' not in data:
        return "404 not found: Can't find plant_id!"
    plant_id = data.get("plant_id")
    return get_plant_process_list(mycursor, plant_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
