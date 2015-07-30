import send_text
import urllib2
import json
import time


def tube(number, message):

    response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
    data = json.load(response)

    switch = False
    
    if (message.lower() == "hammersmith and city") or (message.lower() == "hammersmith") or (message.lower() == "hammersmith & city"):
        message = "hammersmith-city"

    if (message.lower() == "waterloo and city") or (message.lower() == "waterloo") or (message.lower() == "waterloo & city"):
        message = "waterloo-city"

    for x in data:
        if x["id"] == message.lower():
            switch = True
            print x["name"]
            print x["lineStatuses"][0]["statusSeverityDescription"]
        send = x["name"].title() + " Line: " + x["lineStatuses"][0]["statusSeverityDescription"]
        if "reason" in x["lineStatuses"][0]:
            print "Reason sent"
            send2 = "Issue: " + x["lineStatuses"][0]["reason"]
        send = x["name"].title() + " Route: " + x["lineStatuses"][0]["statusSeverityDescription"]

        if switch is True:
            send_text.text(number, send)
            
            if "reason" in x["lineStatuses"][0]:
                time.sleep(3)
                send_text.text(number, send2)

        if switch is False:
            send_text.text(number, 'Not a real line!')
