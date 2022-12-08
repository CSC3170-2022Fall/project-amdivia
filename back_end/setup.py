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

if __name__ == "__main__":
  app.run()
