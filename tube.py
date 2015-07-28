import send_text
import urllib2
import json

def tube(number, message):
	
	switch = False
	line = message[1]

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)   
	print 

	line = line.lower()

	for x in data:
		if x["name"]==line:
			switch = True
			print x["name"]
			print x["lineStatuses"][0]["statusSeverityDescription"]

			send = x["name"] + " Line Status: " + x["lineStatuses"][0]["statusSeverityDescription"]
	
	if switch is True:
		send_text.text(number, send)
		
	if switch is False:
		print "Whoops! Error made."
		send_text.text(number, "Failed.")
