from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    if data is None or 'name' not in data or 'password' not in data:
        return 'must post with name/password params'
    name = data['name']
    password = data['password']
    return name + password

@app.route("/bank/check", methods=['POST'])
def check():
    data = request.get_json()
    if data is None or 'name' not in data or 'id' not in data:
        return 'error'
    name = data['name']
    id = data['id']
    
    return name + id

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5002, debug = True)
