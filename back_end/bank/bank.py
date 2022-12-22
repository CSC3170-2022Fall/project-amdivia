import json
import pymysql
from flask import Flask, request
from connector import *

app = Flask(__name__)

def create_table(cursor):
    sql = "create AMDVIA.bank(consumer_ID int(8) not null, account_balance int, CONSTRAINT operation_PK primary key (consumer_ID))"
    cursor.execute(sql)

def check_account(cursor, con_id):
    sql = """
    select account_balance
    from AMDVIA.bank
    where consumer_ID = """ + str(con_id)
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 0:
        return "404 not found: The consumer_ID doesn't exist!"
    return results[0][0]

def insert_account(cursor, con_id, acc_bal):
    sql = """
    insert into AMDVIA.bank(consumer_ID, account_balance) values(""" + str(con_id) + ", " + str(acc_bal) + ")"
    print(sql)
    cursor.execute(sql)
    mydb.commit()

def pay(cursor, con_id, cost):
    acc_bal = check_account(cursor, con_id)
    if (acc_bal < cost):
        return "503 service unavailable: The account doesn't have enough money!"
    acc_bal = acc_bal - cost
    sql = """
    update AMDVIA.bank set account_balance = """ + str(acc_bal) + """
    where consumer_ID = """ + str(con_id)
    cursor.execute(sql)
    mydb.commit()
    return "successful"

