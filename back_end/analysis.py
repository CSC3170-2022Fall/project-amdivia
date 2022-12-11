import numpy as np
import random as rd
import pandas as pd
import seaborn as sns
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
import math
from connector import *

SIMULATION_RANGE = 10
SIMULATION_TIMES = 500
OPERATION_TYPE = 5


class chip:
    def __init__ (self, chip_type, oplist):
        self.type = chip_type
        self.oplist = oplist    # a chip type corresponds to an oplist

class to_plant:
    def __init__ (self, capacity, process_list, loc1, loc2, rate):
        # self.expense = op_expense
        self.capacity = capacity # capacity means the amount of work can be done in certain unit time, e.g. 100 chips / day
        self.process_list = process_list # [(20, 30),(40, 50)] means the plant has two time intervals occupied.
        self.loc1 = loc1
        self.loc2 = loc2
        self.rate = rate

class chip_in_package:                  # package is a list of chip_in_package
    def __init__ (self, oplist, chip_number, time_list, plant_info):
        self.oplist = oplist
        self.number = chip_number
        self.timelist = time_list        # start_time for each operation. The length of it is equal to which of oplist
        self.plant = plant_info          # it's a list, the aimed plant for each operation

class consumer: # need consumber's loc
    def __init__ (self, package, loc1, loc2):
        self.package = package
        self.loc1 = loc1
        self.loc2 = loc2

def insert_time (list, x, y):       # add (x, y) interval into the list, and keep it in order
    for i in range(len(list)):
        if list[i][1] > x:
            list.insert(i, (x, y))
            return
    list.append((x, y))
# e.g. list = [(1, 2), (3, 4), (7, 8)]
# insert_time(list, 5, 6) cause the list become list = [(1, 2), (3, 4), (5, 6), (7, 8)]
# the list is the process list, in which every two intervals have no overlap

def delete_time (list, x, y):     # similar as insert_time but delete an existed interval (x, y), ensure (x, y) is in list
    for i in range(len(list)):
        if list[i][0] == x and list[i][1] == y:
            list.pop(i)
            break


# time
def allocate_package_time (package, loc1, loc2):
    cost_distribution = [] # cost_distribution
    time_distribution = [] # time_distribution records for the time every simulation is done.
    for i in range(SIMULATION_TIMES):
        stack = [] # record the interval added temporarily in simulation part.
        latest_time = [] # the latest time all operations are done in the simulation
        package = np.random.permutation(package) # randomize the order of chip selection.
        cost = 0
        last_plant = None
        for chip in package:
            last_time = 0           # In real simulation, it should be "current time"
            for op in chip.oplist:
                # retrieve the valid plant for each operation
                time_cost, money_cost, plant_list = get_op_cost_plant(mycursor, op)

                plant_id = rd.choice(plant_list) # randomly choose a valid plant
                plant = to_plant(*get_plant_info(mycursor, plant_id))
                if last_plant != None:
                    op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*time_cost*5*plant.rate/10+((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))  # calculate the operation time in the plant, need to ensure number > 0 (otherwise why you buy it?)
                    cost += (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*money_cost*5*plant.rate/10 + ((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))
                else:
                    op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*time_cost*5*plant.rate/10))
                    cost += (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*money_cost*5*plant.rate/10))
                last_plant = plant
                # find the left_time-th valid time to be the start time of the operation
                left_time = rd.randint(1, SIMULATION_RANGE)
                choose_time = -1        # The time we finally choose
                for x, y in plant.process_list:
                    if x - op_time - last_time + 1 < left_time: # the chosen time is not in this interval
                        left_time -= max(0, x - last_time - op_time + 1)
                        last_time = y
                    else: # the chosen time is in this interval
                        choose_time = left_time + last_time - 1
                        left_time = 0
                        break

                if left_time > 0: # if there is still left_time after finding all intervals
                    choose_time = left_time + last_time - 1
                last_time = choose_time + op_time
                insert_time(plant.process_list, choose_time, choose_time + op_time)
                # the simulation inserts the time interval temporarily, it should be removed later.
                stack.append((plant.process_list, choose_time, choose_time + op_time))
            last_time += ((last_plant.loc1-loc1)**2+(last_plant.loc2-loc2)**2)**0.5  #add the consumer time
            cost += ((last_plant.loc1-loc1)**2+(last_plant.loc2-loc2)**2)**0.5
            latest_time.append(last_time)
              #  if i == 20: print(plant.ID, plant.process_list, latest_time)
        latest_time = max(latest_time)
        # delete the temporary interval before the next simulation
        for list, x, y in stack:
            delete_time(list, x, y)
        time_distribution.append(latest_time)
        cost_distribution.append(cost)

    return time_distribution,cost_distribution  # this line is to find the time distribution of simulation

def calculate_user_info(kde_t,kde_m,status,package,loc1,loc2):
    user_latest_time = [] # the latest time all operations are done in the user given timelist
    # calculate the user_latest_time
    cost = 0
    for chip in package:
        last_op_finish_time = 0  # this should be current time
        last_plant = None
        for i in range(len(chip.plant)):
            plant_info = chip.plant[i]
            time_info = chip.timelist[i]
            op_info = chip.oplist[i]
            plant = to_plant(*get_plant_info(mycursor, plant_info))  # find the current plant's info
            time_cost, money_cost, plant_list = get_op_cost_plant(mycursor, chip.oplist[i])
            if last_plant == None:
                op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*time_cost*5*plant.rate/10))
                cost += (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*money_cost*5*plant.rate/10))
            else:
                op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*time_cost*5*plant.rate/10+((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))
                cost += (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*money_cost*5*plant.rate/10+((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))
            last_plant = plant
            if status == 'commit':
                update_time(plant_info, time_info, time_info + op_time) # the user's add has the effect on the process_list
            last_op_finish_time = time_info + op_time
        last_op_finish_time += ((last_plant.loc1-loc1)**2+(last_plant.loc2-loc2)**2)**0.5
        cost += ((last_plant.loc1-loc1)**2+(last_plant.loc2-loc2)**2)**0.5
        user_latest_time.append(last_op_finish_time)
    user_latest_time = max(user_latest_time)
    score_t = 1-kde_t.integrate_box_1d(0,user_latest_time)
    score_m = 1-kde_m.integrate_box_1d(0,cost)
    return 0.5*(score_m+score_t)*100,user_latest_time,cost

def calc_kpi (package_full_list, loc1, loc2):
    me = consumer(package_full_list, loc1, loc2)
    dis_t, dis_m = allocate_package_time(me.package, me.loc1, me.loc2)
    kde_t = gaussian_kde(dis_t)
    kde_m = gaussian_kde(dis_m)
    score, time, cost = calculate_user_info(kde_t,kde_m,'analysis',me.package,loc1,loc2)
    return score
