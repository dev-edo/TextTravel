#Needs to be linked to the texting service, planned for a later date but needs to be done before
#friday. -Mike

import send_text
import urllib2
import json

def bus(number, message):
	
	switch = False
	route = message[1]

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/bus/status')
	data = json.load(response)   
	print 

	route = route.lower()

	for x in data:
		if x["id"]==route:
			switch = True
			print x["name"]
			print x["lineStatuses"][0]["statusSeverityDescription"]

			send = x["name"] + ": " + x["lineStatuses"][0]["statusSeverityDescription"]
			
	if switch is True:
		send_text.text(number, send)
		
	if switch is False:
		print "Whoops! Error made."
		send_text.text(number, "Not a real route No.!")
