import numpy as np
import random as rd
"""
TO DO LIST
insert the time interval into the process list in order
random data generator
"""

SIMULATION_RANGE = 5


class chip:
    def __init__ (self, chip_type, oplist):
        self.type = chip_type
        self.oplist = oplist

class plant:
    def __init__ (self, name, op_type, capacity, process_list):
        self.name = name
        self.type = op_type
        self.capacity = capacity
        self.process_list = process_list

class chip_in_package:                  # package is a list of chip_in_package
    def __init__ (self, chip_type, chip_number, time_list):
        self.type = chip_type
        self.number = chip_number
        self.timelist = time_list                           # time_list: start_time for each operation

#def data_generate ():

def allocate_package (package):
    global chip_full_list
    global plant_full_list
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
            
            op_time = (chip.number - 1) / plant.capacity + 1;  # need to ensure number > 0
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
            if left_time > 0:
                choose_time = left_time + last_time - 1
            
            #insert_time(plant.process_list, choose_time, choose_time + op_time)
            # use stack to record the simulation
            #delete_time(plant.process_list, choose_time, choose_time + op_time)
            

chip_full_list = [chip(1, [1, 2, 3]), chip(2, [1, 4, 3])]
plant_full_list = [plant("a", 1, 30, []), plant("b", 2, 50, []), plant("c", 3, 70, []), plant("d", 4, 90, [])]
package_full_list = [ [ chip_in_package(1, 110, [0, 50, 100]), chip_in_package(2, 350, [0, 70, 200]) ], [ chip_in_package(1, 200, [60, 90, 110]) ] ]

for package in package_full_list:
    allocate_package(package)
    
