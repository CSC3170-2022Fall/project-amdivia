from faker import Faker
import numpy as np
import pandas as pd
import random

fk = Faker("en_US")

# consumer table, 100个
# 8位int, sample可以保证唯一性
consumer_id = random.sample(range(10000000, 99999999), 100)
consumer_password = random.sample(range(100000, 999999), 100)
# string
first_name = [fk.first_name() for i in range(100)]
# string
second_name_lib = [
    'Cechtelar', 'Smith', 'Jones', 'Taylor', 'Williams', 'Brown', 'Davies',
    'Evans', 'Wilson', 'Thomas', 'Robinson', 'Thompson', 'White', 'Green',
    'Harris', 'Clarke', 'Jackson', 'Patel', 'Trump', 'Miller', 'Bell',
    'Simpson', 'Marshall', 'Bennett', 'Robertson', 'Lloyd', 'Graham', 'Rogers',
    'Mason', 'Saunders'
]
second_name = random.choices(second_name_lib, k=100)
# 8位int, sample可以保证唯一性
bank_id = random.sample(range(10000000, 99999999), 100)
# int 1~1000
loc1 = np.random.randint(1, 1000, size=100)
loc2 = np.random.randint(1, 1000, size=100)
consumer = pd.DataFrame(
    np.array([consumer_id, consumer_password, first_name, second_name, bank_id, loc1, loc2]).T,
    columns=[
        'consumer_id', 'consumer_password', 'first_name', 'second_name', 'bank_id', 'loc1', 'loc2'
    ])
consumer.to_csv('./consumer.csv')

# # order table, 200个（一个consumer可以有多个order）undo
# # 8位int, sample可以保证唯一性
# order_id = random.sample(range(10000000, 99999999), 200)
# consumer_id_order = random.choices(consumer_id, k=200)
# # 1-下单成功且已完成, 0-下单成功但未完成
# status = random.choices([0, 1], k=200)
# success = [i for i in range(200) if status[i] == 1]
# process = [i for i in range(200) if status[i] == 0]
# # package list
# # 所有的package
# tmp_list = [i for i in range(10000000, 99999999)]
# package_list = []
# for i in range(200):
#     # 最多5种芯片
#     tmp_package_id = []
#     for j in range(random.randint(0, 5)):
#         tmp_package = random.choice(tmp_list)
#         tmp_package_id.append(tmp_package)
#         tmp_list.remove(tmp_package)
#     package_list.append(tmp_package_id)


# # package table undo


# chip table 12种
operation_sequence = []
for i in range(12):
    list = random.sample(range(50), random.randint(3, 8))
    list.sort()
    operation_sequence.append(list)
chip_name = ['CK101', 'UH677', 'DM878', 'NAD981', "OBY558", 
            'NB666','UZ235', 'QE431','WR976', 'POE87', 
            'EQW878', 'ZOI253']
chip = pd.DataFrame()
chip['chip_name'] = chip_name
chip['operation_sequence'] = operation_sequence
chip.to_csv('./chip.csv')


# operation table 50
operation_id = [i for i in range(50)]
time_cost = np.random.randint(20,100,size=50) # op time 20-100
money_cost = np.random.randint(100,200,size=50) # op money 100-200
plant_list = []
for i in range(50):
    list = random.sample(range(200), random.randint(5, 15))
    list.sort()
    plant_list.append(list)
operation = pd.DataFrame()
operation['operation_id'] = operation_id
operation['time_cost'] = time_cost
operation['money_cost'] = money_cost
operation['plant_list'] = plant_list
operation.to_csv('./operation.csv')


# plant table 200个
plant_id = [i for i in range(200)]
plant_name = [fk.unique.company() for i in range(200)]
capacity = [random.randint(200, 1000) for i in range(200)] # capacity 200-1000
process_list = []
for i in range(200):
    process_list.append([])
processing_rate = [random.randint(1,10) for i in range(200)] # rate 1 10
loc1 = np.random.randint(1, 1000, size=200) # loc 1-1000
loc2 = np.random.randint(1, 1000, size=200)
plant = pd.DataFrame()
plant['plant_id'] = plant_id
plant['plant_name'] = plant_name
plant['capacity'] = capacity
plant['process_list'] = process_list
plant['processing_rate'] = processing_rate
plant['loc1'] = loc1
plant['loc2'] = loc2
plant.to_csv('./plant.csv')