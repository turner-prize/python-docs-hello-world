from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    data = request.data
    dataDict = json.loads(data)
    x = int(dataDict['key']) * int(dataDict['key'])
    r = requests.get("https://www.google.com")
    return str(x)
