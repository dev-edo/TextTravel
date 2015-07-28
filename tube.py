import send_text
import urllib2
import json

def tube(number, message):
	
	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)
	print "Possible line sent: " + line

	switch = False
	line = line.lower()

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
		send_text.text(number, message="Not a real line!")
