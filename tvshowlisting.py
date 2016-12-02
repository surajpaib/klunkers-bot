import requests
import datetime


t=datetime.datetime.now()
def tvlisting(channel):
    channel=channel.lower()
    channel=channel.replace(" ","-")
    date=t.day+"/"+t.month+"/"+t.year
    tv=requests.get("http://indian-television-guide.appspot.com/indian_television_guide?channel="+channel-name+"&date"+date)
    return tv.content
