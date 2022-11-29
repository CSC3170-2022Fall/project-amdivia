import numpy as np
import random as rd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

SIMULATION_RANGE = 10
SIMULATION_TIMES = 5000
OPERATION_TYPE = 5


class chip:
    def __init__ (self, chip_type, oplist):
        self.type = chip_type
        self.oplist = oplist    # a chip type corresponds to an oplist

class plant:
    def __init__ (self, plant_ID, op_type, capacity, process_list,loc1,loc2,rate):
        self.ID = plant_ID
        self.type = op_type
        self.capacity = capacity # capacity means the amount of work can be done in certain unit time, e.g. 100 chips / day
        self.process_list = process_list # [(20, 30),(40, 50)] means the plant has two time intervals occupied.
        self.loc1 = loc1
        self.loc2 = loc2
        self.rate = rate

class chip_in_package:                  # package is a list of chip_in_package
    def __init__ (self, chip_type, chip_number, time_list, plant_info):
        self.type = chip_type           
        self.number = chip_number
        self.timelist = time_list        # start_time for each operation. The length of it is equal to which of oplist 
        self.plant = plant_info          # it's a list, the aimed plant for each operation
        
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

def allocate_package (package):
    global chip_full_list # the list records all chip information
    global plant_full_list # the list records all plant information
    global op_to_plant
    for plant in plant_full_list:
        for type in plant.type:
            op_to_plant[type].append(plant)
            
    time_distribution = [] # time_distribution records for the time every simulation is done.
    for i in range(SIMULATION_TIMES):
        stack = [] # record the interval added temporarily in simulation part.
        latest_time = 0 # the latest time all operations are done in the simulation
        package = np.random.permutation(package) # randomize the order of chip selection.
        for chip in package:
            # find the oplist for this chip
            oplist = []
            last_plant = None
            for chip_info in chip_full_list:
                if chip_info.type == chip.type:
                    oplist = chip_info.oplist
            
            last_time = 0           # In real simulation, it should be "current time"
            for op in oplist:
                # retrieve the valid plant for each operation
                plant_list = op_to_plant[op]
                        
                plant = rd.choice(plant_list) # randomly choose a valid plant
                
                """ mode 1
                op_time = ((chip.number - 1) // plant.capacity + 1)
                if last_plant != None:
                    op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*op*5*plant.rate/10+((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))  # calculate the operation time in the plant, need to ensure number > 0 (otherwise why you buy it?)
                else:
                    op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*op*5*plant.rate/10))
                """
                """ mode 2
                op_time = ((chip.number - 1) // plant.capacity + 1)
                if last_plant != None:
                    op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)+((last_plant.loc1-plant.loc1)**2+(last_plant.loc2-plant.loc2)**2)**0.5))  # calculate the operation time in the plant, need to ensure number > 0 (otherwise why you buy it?)
                else:
                    op_time = ((chip.number - 1) // plant.capacity + 1)
                """
             #   """ mode 3
                op_time = (int)(math.ceil(((chip.number - 1) // plant.capacity + 1)*op*5*plant.rate/10))
            #    """
                """ mode 4 
                op_time = ((chip.number - 1) // plant.capacity + 1)
                """
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
                last_time = choose_time
                insert_time(plant.process_list, choose_time, choose_time + op_time)
                # the simulation inserts the time interval temporarily, it should be removed later.
                stack.append((plant.process_list, choose_time, choose_time + op_time)) 
                latest_time = max(latest_time, choose_time + op_time) 
              #  if i == 20: print(plant.ID, plant.process_list, latest_time)
        
        # delete the temporary interval before the next simulation
        for list, x, y in stack:
            delete_time(list, x, y)
        time_distribution.append(latest_time)
        
    time_distribution.sort()
    
    return time_distribution  # this line is to find the time distribution of simulation
    
    user_latest_time = 0 # the latest time all operations are done in the user given timelist
    # calculate the user_latest_time
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
            insert_time(plant.process_list, time_info, time_info + op_time) # the user's add has the effect on the process_list
            user_latest_time = max(user_latest_time, time_info + op_time)
#    print(user_latest_time)
    # find the rank of the user_latest_time in the time_distribution, and get the score
    for i in range(len(time_distribution)):
        if user_latest_time <= time_distribution[i]:
            return 1 - i / len(time_distribution)
    return 0     

chip_full_list = []
plant_full_list = []
op_to_plant = {i:[] for i in range(OPERATION_TYPE)}
# chip 1, amount = 1000, start 3 operations at [1000,2000,3000] respectively, in plant [2,7,13]
# you can modify the package_full_list. The later two arguement don't affect the time_distribution(since that's user's decision)
package_full_list = [[chip_in_package(1, 1000, [1000,2000,3000], [2,7,13])]] 

# some small data, has score > 0
# chip_full_list = [chip(1, [1, 2, 3]), chip(2, [1, 4, 3])]
# plant_full_list = [plant(1, 1, 30, []), plant(2, 2, 50, []), plant(3, 3, 70, []), plant(4, 4, 90, [])]
# package_full_list = [ [ chip_in_package(1, 110, [2, 2, 3], [1,2,3]), chip_in_package(2, 350, [6, 0, 5], [1, 4, 3]) ], [ chip_in_package(1, 200, [20,20,20], [1,2,3]) ] ]

# read from the data
fig = sns.boxplot()
for data in range(1,4):
    d1 = pd.read_csv("./info_plant"+str(data)+".csv")
    for i in range(200):
        plant_full_list.append(plant(i, eval(str(d1["type"][i])), d1["capacity"][i], eval(str(d1["status"][i])), d1["loc1"][i], d1["loc2"][i], d1["rate"][i]))
    d2 = pd.read_csv("./info_chip.csv")
    for i in range(12):
        chip_full_list.append(chip(d2["type"][i], eval(d2["oplist"][i])))
   # print
    for package in package_full_list:
        dis = allocate_package(package)
    print(dis)   
    dis = np.array(dis)
    x,y=np.unique(dis,return_counts=True)
    fig=sns.kdeplot(dis,legend=str(data))
    plt.legend(str(data))
   # sns.displot(dis,bins=len(y),kde=True)
plt.show()
