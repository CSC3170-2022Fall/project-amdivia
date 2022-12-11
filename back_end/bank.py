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

