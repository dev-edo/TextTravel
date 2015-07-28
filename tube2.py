import urllib2
import json
import send_text

def tube(number,spl_text):

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)   
	print 

	line = spl_text[1]

	for x in data:
		if x["id"]==line:
			send_text.text(number, ["lineStatuses"][0]["statusSeverityDescription"])
	return



