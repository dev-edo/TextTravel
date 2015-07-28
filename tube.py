import send_text
import urllib2
import json

def tube(number, message):
	
	switch = False
	
	line = message[1]
	line = line.lower()
	
	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)
	
	for x in data:
		if x["id"] == line:
			switch = True
			print x["name"]
			print x["lineStatuses"][0]["statusSeverityDescription"]
			
	send = line.title() + " Line: " + x["lineStatuses"][0]["statusSeverityDescription"]
	
	if switch is True:
		send_text.text(number, send)
		
	if switch is False:
		print "Whoops! Error made."
		send_text.text(number, "Not a real line!")
