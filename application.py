from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    data = request.data
    dataDict = json.loads(data)
    return dataDict['key']
