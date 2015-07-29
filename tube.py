import send_text
import urllib2
import json


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

    if switch is True:
        send_text.text(number, send)

    if switch is False:
        send_text.text(number, 'Error: Not a real line!')
