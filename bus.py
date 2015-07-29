import send_text
import urllib2
import json


def bus(number, item):
    message = item
    response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/bus/status')
    data = json.load(response)

    switch = False

    for x in data:
        if x["id"] == message.lower():
            switch = True
            print x["name"]
            print x["lineStatuses"][0]["statusSeverityDescription"]
            send = x["name"].upper() + " Route: " + x["lineStatuses"][0]["statusSeverityDescription"]

    if switch is True:
        send_text.text(number, send)

    if switch is False:
        print "Whoops! Error made."
        send_text.text(number, "Not a real route!")
