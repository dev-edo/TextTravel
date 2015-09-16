import send_text, urllib2, json, time

def tube(number, message):
    
    switch = False

    response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
    data = json.load(response)
    print "Possible route no. sent: " + message
    
    if (message.lower() == "hammersmith and city") or (message.lower() == "hammersmith") or (message.lower() == "hammersmith & city"):
        message = "hammersmith-city"

    if (message.lower() == "waterloo and city") or (message.lower() == "waterloo") or (message.lower() == "waterloo & city"):
        message = "waterloo-city"

    for x in data:
        if x["id"] == message.lower():
            message.lower()
            switch = True
            print x["name"]
            print x["lineStatuses"][0]["statusSeverityDescription"]
            if "reason" in x["lineStatuses"][0]:
                switch = True
                print "Reason sent"
                send2 = "Issue: " + x["lineStatuses"][0]["reason"]
        send = message.title() + " Line: " + x["lineStatuses"][0]["statusSeverityDescription"]


    if switch is True:
        send_text.text(number, send)
        if "reason" in x["lineStatuses"][0]:
            time.sleep(3)
            send_text.text(number, send2)

    if switch is False:
        print "Error."
        send_text.text(number, "Not a real line!")
