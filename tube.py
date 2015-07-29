import send_text
import urllib2
import json

def tube(number, message):

    response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
    data = json.load(response)

    switch = False
    line = message
    
    
    if (line.lower() == "hammersmith and city") or (line.lower() == "hammersmith") or (line.lower() == "hammersmith & city"):
        line = "hammersmith-city"

    if (line.lower() == "waterloo and city") or (line.lower() == "waterloo") or (line.lower() == "waterloo & city"):
        line = "waterloo-city"

    for x in data:
        if x["id"] == line.lower():
            switch = True
            print x["name"]
            print x["lineStatuses"][0]["statusSeverityDescription"]
        send = x["name"].title() + " Line: " + x["lineStatuses"][0]["statusSeverityDescription"]

    if switch is True:
        send_text.text(number, send)

    if switch is False:
        send_text.text(number, 'Error: Not a real line!')
