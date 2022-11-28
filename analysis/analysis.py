import numpy as np
import random as rd
import pandas as pd

SIMULATION_RANGE = 10
SIMULATION_TIMES = 1000


class chip:
    def __init__ (self, chip_type, oplist):
        self.type = chip_type
        self.oplist = oplist

class plant:
    def __init__ (self, plant_ID, op_type, capacity, process_list):
        self.ID = plant_ID
        self.type = op_type
        self.capacity = capacity
        self.process_list = process_list

class chip_in_package:                  # package is a list of chip_in_package
    def __init__ (self, chip_type, chip_number, time_list, plant_info):
        self.type = chip_type
        self.number = chip_number
        self.timelist = time_list                           # time_list: start_time for each operation
        self.plant = plant_info
        
def insert_time (list, x, y):
    for i in range(len(list)):
        if list[i][1] > x:
            list.insert(i, (x, y))
            return
    list.append((x, y))

def delete_time (list, x, y):
    for i in range(len(list)):
        if list[i][0] == x and list[i][1] == y:
            list.pop(i)
            break

def allocate_package (package):
    global chip_full_list
    global plant_full_list
        
    time_distribution = []
    for i in range(SIMULATION_TIMES):
        latest_time = 0
        stack = []
        package = np.random.permutation(package)
        for chip in package:
            # find the oplist for this chip
            oplist = []
            for chip_info in chip_full_list:
                if chip_info.type == chip.type:
                    oplist = chip_info.oplist
            # retrieve the valid plant (sql)
            for op in oplist:
                plant_list = []
                for plant in plant_full_list:
                    if plant.type == op:
                        plant_list.append(plant)
                plant = rd.choice(plant_list)
               
                op_time = (chip.number - 1) // plant.capacity + 1;  # need to ensure number > 0
                
                last_time = 0          # In real simulation, it should be "current time"
                left_time = rd.randint(1, SIMULATION_RANGE)
                choose_time = -1
                for x, y in plant.process_list:
                    if x - op_time - last_time + 1 < left_time:
                        left_time -= max(0, x - last_time - op_time + 1)
                        last_time = y
                    else:
                        choose_time = left_time + last_time - 1
                        left_time = 0
                        break
                if left_time > 0:
                    choose_time = left_time + last_time - 1
                insert_time(plant.process_list, choose_time, choose_time + op_time)
                stack.append((plant.process_list, choose_time, choose_time + op_time))
                latest_time = max(latest_time, choose_time + op_time) 
              #  if i == 20: print(plant.ID, plant.process_list, latest_time)
                
        for list, x, y in stack:
            delete_time(list, x, y)
        time_distribution.append(latest_time)
        
    time_distribution.sort()
    
    return time_distribution  # this line is to find the time distribution of simulation
    
    user_latest_time = 0
    for chip in package:
        for i in range(len(chip.plant)):
            plant_info = chip.plant[i]
            time_info = chip.timelist[i]
            capacity = 0
            for plant in plant_full_list:
                if plant.ID == plant_info:
                    capacity = plant.capacity
                    break
            op_time = (chip.number - 1) // capacity + 1;
            insert_time(plant.process_list, time_info, time_info + op_time)
            user_latest_time = max(user_latest_time, time_info + op_time)
#    print(user_latest_time)
    for i in range(len(time_distribution)):
        if user_latest_time <= time_distribution[i]:
            return 1 - i / len(time_distribution)
    return 0     

chip_full_list = []
plant_full_list = []
package_full_list = [[chip_in_package(1, 1000, [1000,2000,3000], [2,7,13])]] # chip 1, amount = 1000, start 3 operations at [1000,2000,3000] respectively, in plant [2,7,13].
# chip_full_list = [chip(1, [1, 2, 3]), chip(2, [1, 4, 3])]
# plant_full_list = [plant(1, 1, 30, []), plant(2, 2, 50, []), plant(3, 3, 70, []), plant(4, 4, 90, [])]
# package_full_list = [ [ chip_in_package(1, 110, [2, 2, 3], [1,2,3]), chip_in_package(2, 350, [6, 0, 5], [1, 4, 3]) ], [ chip_in_package(1, 200, [20,20,20], [1,2,3]) ] ]
d1 = pd.read_csv("./info_plant.csv")
for i in range(200):
    plant_full_list.append(plant(i, d1["type"][i], d1["capacity"][i], eval(str(d1["status"][i])) ))
d2 = pd.read_csv("./info_chip.csv")
for i in range(12):
    chip_full_list.append(chip(d2["type"][i], eval(d2["oplist"][i])))

for package in package_full_list:
    print(allocate_package(package))

