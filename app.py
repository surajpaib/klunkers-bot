import requests
import json
from flask import Flask, request
from tvshowlisting import tvlisting
import os

app=Flask(__name__)


@app.route("/webhook",methods=['GET','POST'])
def webhook():
    if (request.method=='POST'):
        data=request.get_json()
        result=data["result"]
        action=result["action"]
        channel=result["parameters"]["channel"]
        show=tvlisting(channel)
        obj={
            'speech':"The TV show playing right now is"+show
            'displayText':"The show that's playing right now is"
            'data':{'facebook':{'TV show playing now is'+show}}
            'contextOut': None
            'source': None

        }


        response=json.dumps(obj)
        return response
    if (request.method=='GET'):
        return "Page is online"


@app.route("/")
def index():
    return "Server is now Online"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
