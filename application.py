from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    data = request.data
    dataDict = json.loads(data)
    x = int(dataDict['key']) * int(dataDict['key'])
    r = requests.get("https://fantasy.premierleague.com/drf/elements/")
    r = r.json()
    #return str(x)
    return str(r)
