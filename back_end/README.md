# Database Design
## ER diagram
![image](https://github.com/CSC3170-2022Fall/project-amdvia/blob/740d8731b1090dbdaf137a537adce1d91d61b42d/res/er_diagram.png)
Here shows our ER diagram of the main database. We could start from the consumer table. As you can see, consumer table include a unique ID, and other necessary information including location, bank ID and so on. It has a one to many relationship with the order table. Since each order must has a consumer, one consumer can have several orders and some consumer might not have any orders. Here one order contains many types of chips. So we need to depart orders into different packages, where one package only contain one type of chip. So one order can have one to many packages, and each package must belong to one order. We also use unique order and package ID as primary key. Then we can tell that each package must have one type of chip, and one chip need several operations to produce it. Last but not least, operations need to be done by plants. Since one type of machine can do several types of operation, and one operation can be done by different plants, this is a many to many relationship.
## Reduce to Relation Schema
![image](https://github.com/CSC3170-2022Fall/project-amdvia/blob/main/res/Main_Database.png)
Then we designed the relation schema. The orange attributes are multi-valued attributes that stored as Jason. The dash lines indicate the original foreign keys. 
Actually, we don’t use tables to represent the relationship in the ER diagram. Instead, we use these list, for example, process list, package list to store it as an attribute without normalization. Also, the reason why we use dash line to indicate the foreign keys is that we don’t use any foreign keys in implementation.

Firstly, for no normalization, the reason is that in the analysis of the production plan, we need to extract these information frequently. If we depart the relationship into several tables, we need to do many natural joins when we extract the information, which is a waste of time. Instead, stored them as multi-valued attributes results easier and faster extraction in analysis.

Besides, we don’t use any foreign key constraint because our database don’t allow any input that violate the constraints. More specifically, users are only allowed to select the legal information that are already settled in our system at the front end, the referenced attribute will be determined all by our system instead of customer themselves. This means violation of foreign key constraints will not happen! This ease our database and increase the processing time in the analysis. Also, since the referencing attributes such as operations of each type of machine are stored as list in Jason, it’s hard for mysql to check the foreign key constraints.

# bank module

### file: bank.py initialze_bank/initial_bank.py

bank.py: Include the necessary functions for the bank module. "create_table" for creating bank table in database, "insert_account" for
creating a new account in database, "check_account" for querying such account_id's balance and "pay" for debitting the corresponding account_id

initial_bank.py: Initialize the bank database. Provide fake data in the bank account corresponding to the customer.

![image](https://github.com/CSC3170-2022Fall/project-amdvia/blob/740d8731b1090dbdaf137a537adce1d91d61b42d/res/bank_diagram.png)

# back end

file: back.py, connector.py, analysis.py

back.py: Provide the api for different requests.

connector.py: Interact with databse and request by functions.

analysis.py: Analysis the plan the user provided. Validate it. If valid, analysis the plan and return kpi.

![image](https://github.com/CSC3170-2022Fall/project-amdvia/blob/main/res/back_end%20diagram.jpg?raw=true)

# 大致流程：
用户提交方案 -> 方案通过并计算出kpi(/kpi) -> 用户确认后，尝试扣款其银行账户(/pay/) -> 扣款成功后，把订单信息写入数据库(/confirm)

# 1. 用户login in前端: 给consumer_id, consumer_passward; 后端返回密码错误(0)，id不存在(2)，成功登录(1)。

接口：[post] http://10.31.133.149:5000/checklogin

## 正确
input
``` json
{
   // 前端发送的json
  "consumer_id": 89638599,
  "consumer_password":706194
}
```
output
```
1
```

## 错误

input
   ```json
{
       "consumer_id":89638599,
       "consumer_password":400820
}
   ```
   output
   ``` json
   0
   ```


## 用户名不存在

input
``` json
{
  "consumer_id": 11111111,
  "consumer_password":706194
}
```
output
``` json
2
```

# 2. 用户切换到订单查询页面，后端返回order的状态。

接口：[get]http://10.31.133.149:5000/order_record?consumer_id=89638599
output
``` json
[(12345678, 89638599, 0, '{"0": 12, "1": 84}', 562229, 60005, 2, 97, 99)]
```
tuple list，每个 tuple 是一个 order

tuple: (order_id, consumer_id, status, package_list, actual_money, budget, order_time, expected_time, finish_time)

## **后续可以改成以dict的形式返回，需要告诉我需要哪几项？**


# 3. 用户切换到工厂信息页面，后端返回当前所有工厂的信息状态。

接口: [get]http://10.31.133.149:5000/plant/process

output:
``` json
{0: [], 1: [], 2: [], 3: [[55, 64], [80, 89]], 4: [], 5: [], 6: [[0, 20], [20, 40]], 7: [[25, 47], [47, 69]], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: [], 26: [], 27: [], 28: [], 29: [], 30: [], 31: [], 32: [], 33: [], 34: [], 35: [], 36: [], 37: [], 38: [], 39: [], 40: [], 41: [], 42: [], 43: [], 44: [], 45: [], 46: [], 47: [], 48: [], 49: [], 50: [], 51: [], 52: [], 53: [], 54: [], 55: [], 56: [], 57: [], 58: [], 59: [], 60: [], 61: [], 62: [], 63: [], 64: [], 65: [], 66: [], 67: [], 68: [], 69: [], 70: [], 71: [], 72: [], 73: [], 74: [], 75: [], 76: [], 77: [], 78: [], 79: [], 80: [], 81: [], 82: [], 83: [], 84: [], 85: [], 86: [], 87: [], 88: [], 89: [], 90: [], 91: [], 92: [], 93: [], 94: [], 95: [], 96: [], 97: [], 98: [], 99: [], 100: [], 101: [], 102: [], 103: [], 104: [], 105: [], 106: [], 107: [], 108: [], 109: [], 110: [], 111: [], 112: [], 113: [], 114: [], 115: [], 116: [], 117: [], 118: [], 119: [], 120: [], 121: [], 122: [], 123: [], 124: [], 125: [], 126: [], 127: [], 128: [], 129: [], 130: [], 131: [], 132: [], 133: [], 134: [], 135: [], 136: [], 137: [], 138: [], 139: [], 140: [], 141: [], 142: [], 143: [], 144: [], 145: [], 146: [], 147: [], 148: [], 149: [], 150: [], 151: [], 152: [], 153: [], 154: [], 155: [], 156: [], 157: [], 158: [], 159: [], 160: [], 161: [], 162: [], 163: [], 164: [], 165: [], 166: [], 167: [], 168: [], 169: [], 170: [], 171: [], 172: [], 173: [], 174: [], 175: [], 176: [], 177: [], 178: [], 179: [], 180: [], 181: [], 182: [], 183: [], 184: [], 185: [], 186: [], 187: [], 188: [], 189: [], 190: [], 191: [], 192: [], 193: [], 194: [], 195: [], 196: [], 197: [], 198: [], 199: []}
```

# 4. 用户切换到下单界面，选择一个chip_name后，后端返回该chip的相关信息，包括，operation 数量， 每个 operation 能被哪些 plant 进行。

接口：[get]http://10.31.133.149:5000/chip/process?chip_type=DM878

   ```json
   // 后端返回的json
   {
       "operation1": [
           "Brown Inc",
           "Davis PLC",
           "Hendricks, Price and Lewis",
           "Miller PLC",
           "Woods Inc"
       ],
       "operation2": [
           "Lowery Ltd",
           "Lowe-Mcintyre",
           "Duncan Ltd",
           "Bridges-Hernandez",
           "Solis-Spencer",
           "Jones Ltd",
           "Watts PLC",
           "Powell Group"
       ],
       "operation3": [
           "Blankenship, Howell and Howell",
           "Fisher, Warren and Moore",
           "Young, Taylor and Jones",
           "Fox Ltd",
           "Ruiz-Jones",
           "Bates, Nelson and Sanchez"
       ],
       "operation4": [
           "Mooney-Taylor",
           "Alvarado PLC",
           "Mckee-Esparza",
           "Robinson LLC",
           "Davis, Murphy and Osborne",
           "George LLC"
       ],
       "operation5": [
           "Reed, Spence and Harris",
           "King-Oneal",
           "Arnold-Carlson",
           "Reed, Johnson and Mitchell",
           "Hall, Woods and Sanchez",
           "Douglas-Franklin",
           "Stone Group",
           "Lewis Inc",
           "Pace, Powell and Stone",
           "Clark-Ford"
       ],
       "operation_number": 5
   }
   ```

# 5. 用户第一次确认下单后，后端check用户的策略是否合理，不合理返回不合理的原因，合理就analysis并返回KPI。合理后会在bank end文件夹生成两个图(money.jpg和time.jpg)表示随机状况下的distribution

# **默认用户选择的工厂是能进行对应 operation 的，此部分只检测 start_time 的合理性**

接口：[post] http://10.31.133.149:5000/kpi

用户的策略合理，则返回一个dict，否则返回一个字符串表示不合理的原因

## 成功
input
   ```json
   // 前端发送的json
   {
    "status":"analysis",   // status 必须为 analysis，否则不会进行分析
    "order_id":12345678,
    "consumer_id":89638599,
    "package_id_list":[12,84],
    "budget":60005,
    "expected_time":97,

    "0_chip_name":"CK101",
    "0_chip_number":50,
    "0_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "0_starttime_list":[0, 25, 55],

    "1_chip_name":"CK101",
    "1_chip_number":30,
    "1_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "1_starttime_list":[20, 47, 80]
    }
   ```
  output
  ``` json
{
    "finishtime_list": [[20,47,64],[40,69,89]],
    "kpi": 84.73384896174014,
    "money_cost": 5622.29,
    "time_cost": 99,
    "validate": true
}
  ```
  
  ## 失败
  input
  ``` json
  {
    "status":"analysis",
    "order_id":12345678,
    "consumer_id":89638599,
    "package_id_list":[12,84],
    "budget":60005,
    "expected_time":97,

    "0_chip_name":"CK101",
    "0_chip_number":50,
    "0_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "0_starttime_list":[0, 25, 55],

    "1_chip_name":"CK101",	
    "1_chip_number":30,
    "1_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "1_starttime_list":[20, 43, 80] //这里第二个数字变成了43
  }
```
output
``` json
the 2-th start time in package 2 in plant "Diaz, Andersen and Cooper" is occupied
```


# 6. 尝试给用户扣款

接口：[post]http://10.31.133.149:5000/bank/pay

input
``` json
{
    "id" : 89638599,
    "money" : 1234 //需要扣的钱
}
```
output
``` json
successful
```

input
``` json
{
    "id" : 89638599,
    "money" : 1234123123
}
```

output
```
503 service unavailable: The account doesn't have enough money!
```


# 7. 在银行扣款后，将订单数据存入 order 和 package 的数据库里（必须在第5，6步成功后才能进行）

input
   ```json
{
    "status":"confirm",
    "order_id":12345678,
    "consumer_id":89638599,
    "package_id_list":[12,84],
    "budget":60005,
    "expected_time":97,
    "money_cost":5622.29,
    "time_cost":99,
    "order_time":2,
    "finishtime_list": [[20,47,64],[40,69,89]],

    "0_chip_name":"CK101",
    "0_chip_number":50,
    "0_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "0_starttime_list":[0, 25, 55],

    "1_chip_name":"CK101",
    "1_chip_number":30,
    "1_plant_name_list":["Reed, Spence and Harris","Diaz, Andersen and Cooper","Fernandez, Boyd and Palmer"],
    "1_starttime_list":[20, 47, 80]
}
   ```

output
```
successful
```
   
# 8. 查询用户的存款(通过conusmer_id)
接口：[get]http://10.31.133.149:5000/bank/check?id=89638599

output
```
897046
```

