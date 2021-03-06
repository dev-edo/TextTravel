import send_text, urllib2, json, time

def bus(number, item):
    
    switch = False

    response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/bus/status')
    data = json.load(response)
    print "Possible route no. sent: " + item

    for x in data:
        if x["id"] == item.lower():
            item.lower()
            switch = True
            print x["name"]
            print x["lineStatuses"][0]["statusSeverityDescription"]
            if "reason" in x["lineStatuses"][0]:
                switch = True
                print "Reason sent"
                send2 = "Issue: " + x["lineStatuses"][0]["reason"]
        send = item.title() + " Route: " + x["lineStatuses"][0]["statusSeverityDescription"]


    if switch is True:
        send_text.text(number, send)
        if "reason" in x["lineStatuses"][0]:
            time.sleep(3)
            send_text.text(number, send2)

    if switch is False:
        print "Error."
        send_text.text(number, "Not a real route!")
