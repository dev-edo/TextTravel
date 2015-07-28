import send_text
import urllib2
import json

def bus(number, messageB):
	
	route = messageB[1]

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/bus/status')
	data = json.load(response)   
	print 

	route = route.lower()

	for x in data:
		if x["id"]==route:
			print x["name"]
			print x["lineStatuses"][0]["statusSeverityDescription"]

			send = x["name"] + ": " + x["lineStatuses"][0]["statusSeverityDescription"]
			send_text.text(number, send)
