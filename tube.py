import send_text
import urllib2
import json

def tube(number, message):
	
	line = message[1]

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)   
	print 

	line = line.lower()

	for x in data:
		if x["id"]==line:
			print x["name"]
			print x["lineStatuses"][0]["statusSeverityDescription"]
			send = line.title() + ": " + x["lineStatuses"][0]["statusSeverityDescription"]

	send_text.text(number, send)
