import numpy as np
import pandas as pd
import random
##-------------------- DATA Generation----------------------------------
capacity = np.random.randint(50,1000,size=200) # with unit chip
type = np.random.randint(0,5,size=200) # type of machine
loc1 = np.random.randint(1,1000,size=200)
loc2 = np.random.randint(1,1000,size=200) #generate location,used to calculate the transformation time, yet it can be implicit in the seperate processing time of each operation
df_factory = pd.DataFrame(np.array([capacity,type,loc1,loc2]).T, columns=['capacity','type','loc1','loc2'])
operation = [[[1,2],20],[[1,3],10],[[2,2],8],[[2,3],15],[[3,2],19]] # five type, [start op, # of op, processing time] the processing time need to be adjusted
factory_status = [] # occupy will be store as [start_time,finish_time],the time must be in ascending order
for i in range(200):
    status = []
    period = np.random.randint(0,10) # # of occupation period
    if period != 0:
        start_and_end = random.sample(range(0,500),2*period)
        start_and_end = np.sort(start_and_end) # gen start and end time for all period
        for j in range(period):
            status.append([start_and_end[2*j],start_and_end[2*j+1]])
    factory_status.append(status) # if period=0, an empty list will be assigned to this factory
df_factory['status'] = factory_status
#print(factory_status) you can print to see the data type and shape
#print(df_factory)
##-------------------------------------------------------------------

#-----------------------outuput to csv--------------------------------
df_factory.to_csv('C:/Users/26741/Desktop/study/hw/CSC3170/program/info.csv') # **PLEASE REPLACE TO YOUR OWN PATH!!**
#-------------------------------------------------------------------------

#---------------- Example to use csv --------------------
#df = pd.read_csv('C:/Users/26741/Desktop/study/hw/CSC3170/program/info.csv')
#proccessing_list = np.array(df['status'])
#print(proccessing_list)
#--------------------------------------------------------



                









