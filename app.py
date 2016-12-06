import requests
import json
from flask import Flask, request
from tvshowlisting import tvlisting
import os

app=Flask(__name__)


@app.route('/webhook',methods=[POST,GET])
def webhook():
    if (request.method==POST):
        data=request.json
        result=data["result"]
        action=result["action"]
        channel=result["parameters"]["channel"]
        show=tvlisting(channel)
        obj={}
        obj["speech"]="The TV show playing right now is"+show
        obj["data"]={"facebook": {"TV show playing now is "+ show}}

        response=json.dumps(obj)
        return response


@app.route('/')
def index():
    return "Server is now Online"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
