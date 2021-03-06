import requests


from flask import Flask, request,Response,jsonify
from tvshowlisting import tvlisting
import os
import json


# Initialize Flask App
app=Flask(__name__)
app.debug=True


# Webhook
@app.route("/webhook",methods=['GET','POST'])
def webhook():
    if (request.method=='POST'):
        data=request.get_json()
        result=data["result"]
        action=result["action"]
        user=data["sessionId"]
        channel=result["parameters"]["channel"]
        show=tvlisting(channel)


        if (show!=None):
            #facebookmsg=json.dumps(facebookmsg)
            obj={
                'speech':"The TV show playing right now is "+show,
                'displayText':"The show that's playing right now is ",
                'data':None,
                'contextOut': None,
                'source': None

                        }
            js=json.dumps(obj)
            resp = Response(js, status=200, mimetype='application/json')
            return resp

        else:
            obj={
                'speech':"Sorry, I cannot find what you are looking for, try another channel?",
                'displayText':"Try another channel please",
                'data':None,
                'contextOut': None,
                'source': None

                        }
            js=json.dumps(obj)
            resp = Response(js, status=200, mimetype='application/json')
            return resp


    if (request.method=='GET'):
        return "Page is online"


@app.route("/")
def index():
    return "Server is now Online"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
