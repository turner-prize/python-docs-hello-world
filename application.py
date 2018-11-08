from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    r = requests.get("https://fantasy.premierleague.com/drf/elements/")
    r = r.json()
    return r[3]