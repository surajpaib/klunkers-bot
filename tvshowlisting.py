import requests
import datetime
import json
from pytz import timezone



'''
tvlisting function that gets current date and time and converts it to Indian Time Zone for Indian TV Guide Listing.
Specifically customized for TV Shows and modified to find nearest match.



'''

def tvlisting(channel):
    t=datetime.datetime.now(timezone('UTC'))
    t=t.astimezone(timezone('Asia/Calcutta'))
    channel=channel.lower()
    channel=channel.replace(" ","-")
    print channel
    year=str(t.year)
    day=t.day
    month=t.month
    if day<10:
        day="0"+str(day)
    if month<10:
        month="0"+str(month)

    date=str(day)+str(month)+year
    print date
    tv=requests.get("http://indian-television-guide.appspot.com/indian_television_guide?channel="+channel+"&date="+date)
    content=json.loads(tv.content)
    time=roundofftime(t)
    print time
    shows=content["listOfShows"]

    for show in shows:
        if (show["showTime"]==time):
            print show["showTitle"]
            return show["showTitle"]







def roundofftime(t):
    if (hour<10):
        hour=t.hour
        hour="0"+hour
    else:
        hour=t.hour

    minute=t.minute
    second="00"

    if (minute)<=30:
        minute="00"

    else:
        minute="30"


    time=str(hour)+":"+str(minute)+":"+str(second)

    return time
