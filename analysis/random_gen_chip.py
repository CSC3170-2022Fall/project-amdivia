import numpy as np
import pandas as pd
import random
##-------------------- DATA Generation----------------------------------
oplist = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [1, 3, 4, 5], [1, 2, 3, 4, 5], [2, 5], [3, 5], [2, 4]]
type = []
for i in range(12):
    type.append(i)
    
df_factory = pd.DataFrame(np.array([type]).T, columns=['type'])
df_factory["oplist"] = oplist

#print(factory_status) you can print to see the data type and shape
#print(df_factory)
##-------------------------------------------------------------------

#-----------------------output to csv--------------------------------
df_factory.to_csv('./info_chip.csv') # **PLEASE REPLACE TO YOUR OWN PATH!!**
#-------------------------------------------------------------------------

#---------------- Example to use csv --------------------
#df = pd.read_csv('C:/Users/26741/Desktop/study/hw/CSC3170/program/info.csv')
#proccessing_list = np.array(df['status'])
#print(proccessing_list)
#--------------------------------------------------------



                









