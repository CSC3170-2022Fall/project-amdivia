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
def KPI_calculator ():
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
        package_full_list.append(chip_in_package(oplist, chip_number, start_time_list, plant_list))
    #print(package_full_list)
    loc1, loc2 = get_consumer_loc(mycursor, consumer_id)
    return str(calc_kpi(package_full_list, loc1, loc2))

@app.route("/bank/check", methods = ['GET'])
def check_id():
    data = request.get_json()
    if data is None or 'id' not in data:
        return "404 not found: Can't find data!"
    return check_account(mycursor, data["id"])

@app.route("/bank/pay", methods = ['POST'])
def check_pay():
    data = request.get_json()
    if data is None or 'id' not in data or 'money' not in data:
        return "404 not found: Can't find data!"
    pay(mycursor, data["id"])

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
    return get_plant_process_list(mycursor, plant_id)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 5001, debug = True)

