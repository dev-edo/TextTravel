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
			send =  line.capwords() + ": " + x["lineStatuses"][0]["statusSeverityDescription"]

	api = clockwork.API('18aee4cf4155c51edb5d460adc9fe06dedea7668')
	message = clockwork.SMS(to = number, message = send)
	response = api.send(message)
