1. 用户login in前端: 给consumer_id, consumer_passward; 后端返回密码错误，id不存在，成功登录。

   ```json
   // 前端发送的json
   {
       "consumer_id":89638599,
       "consumer_password":400820,
   }
   ```

2. 用户切换到订单查询页面，后端返回order的状态。

3. 用户切换到工厂信息页面，后端返回当前所有工厂的信息状态。

4. 用户切换到下单界面，选择一个chipname后，后端返回该chip的相关信息。

   ```json
   // 前端发送GET请求
   GET
   chip_type=DM878
   ```

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

5. 用户第一次确认下单后，后端check策略是否合理，不合理返回不合理的原因，合理就analysis并返回KPI。

   ```json
   // 前端发送的json
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
    "1_starttime_list":[20, 47, 80]
    }
   ```

6. 用户第二次确认下单后，后端询问bank该consumer的余额是否充足，若充足就扣钱并更新bank和淘宝数据库，若不充足就返回余额不足。

   ```json
   // 前端发送的json
   {
       "status":"confirm",
       "order_id":12345678,
       "consumer_id":89638599,
       "package_id_list":[12,84],
       "budge":60005,
       "expected_time":97,
   
       "0_chip_name":"CK101",
       "0_chip_number":50,
       "0_plant_name_list":["dasd","我是工厂名不是id","ad"],
       "0_starttime_list":[0, 3, 9],
   
       "1_chip_name":"NB666",	
       "1_chip_number":30,
       "1_plant_name_list":["fqeq","我是工厂名不是id2"],
       "1_starttime_list":[0, 12, 123],
   }
   ```

   

