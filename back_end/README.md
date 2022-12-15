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

接口: [get]http://10.31.133.149:5000/plant/process?plant_id=7

output:
``` json
[[25, 47], [47, 69]]
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

# 5. 用户第一次确认下单后，后端check用户的策略是否合理，不合理返回不合理的原因，合理就analysis并返回KPI。

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
    "finishtime_list": [[20, 44, 65],[43, 67, 89]],
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


