import json
import pymysql
from flask import Flask, request

app = Flask(__name__)

def create_table(cursor):
    sql = """
    create table if not exists bank(
        consumer_ID int(8) not null,
        account_balance int,
        primary key (consumer_ID)
    );
    """
    cursor.execute(sql)

def check_account(cursor, con_id):
    sql = """
    select account_balance
    from bank
    where consumer_ID = """ + str(con_id)
    check = cursor.execute(sql)
    if (check == 0):
        print("404 not found: The consumer_ID doesn't exist!")
        return -1
    results = cursor.fetchall()
    return results[0][0]

def insert_account(cursor, con_id, acc_bal):
    sql = """
    insert ignore into bank(consumer_ID, account_balance)
    values(""" + str(con_id) + ", " + str(acc_bal) + ")"
    cursor.execute(sql)

def pay(cursor, con_id, cost):
    acc_bal = check_account(cursor, con_id)
    if (acc_bal < cost):
        print("503 service unavailable: The account doesn't have enough money!")
        exit()
    acc_bal = acc_bal - cost
    sql = """
    update bank set account_balance = """ + str(acc_bal) + """
    where consumer_ID = """ + str(con_id)
    cursor.execute(sql)

@app.route("/bank/check", methods = ['POST'])
def check_id():
    data = request.get_json()
    if data is None or 'id' not in data:
        return "404 not found: Can't find data!"
    return check_account(cursor, data["id"])

@app.route("/bank/pay", methods = ['POST'])
def check_pay():
    data = request.get_json()
    if data is None or 'id' not in data or 'money' not in data:
        return "404 not found: Can't find data!"
    pay(data["id"])

if __name__ == "__main__":
    icbc = pymysql.connect(host = '127.0.0.1',
                           port = 3306,
                           user = 'wek_deng',
                           password = '123456',
                           database = 'ICBC')
    cursor = icbc.cursor()
    create_table(cursor)
    app.run()
    icbc.commit()
    cursor.close()
    icbc.close()

