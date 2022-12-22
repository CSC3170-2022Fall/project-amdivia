from connector import *
from bank import *
import pandas as pd
import random

df = pd.read_csv("../fake_data/consumer.csv")
create_table(mycursor)
for i in range(0, df.shape[0]):
    money = random.randint(500000, 1000000)
    insert_account(mycursor, df.iloc[i, 1], money)

