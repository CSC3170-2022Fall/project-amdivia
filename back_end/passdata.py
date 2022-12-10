from flask import Flask, request
import json
from analysis import allocate_package

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

def chiptype_to_opnumber (chip_type):
    # Retrive the operation list according to chip_type (todo) 
    op = 3
    return op
    
    
@app.route("/orderanalysis", methods=['POST'])
def list_to_analysis ():
    data = request.get_json()
    #print(data)
    chip_type = data['chiptype']
    total = chiptype_to_opnumber(chip_type)
    start_time_list = []
    plant_list = []
    for i in range(1, total + 1):
        string = "plant" + str(i)
        plant_list.append(data[string])
        string = "starttime" + str(i)
        start_time_list.append(data[string])
    return str(allocate_package([start_time_list, plant_list]))



if __name__ == "__main__":
  app.run(debug = True)
