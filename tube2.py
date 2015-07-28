import urllib2
import json
import send_text

def tube(number,text_spl):
	line = raw_input('Enter Tube line:')

	response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
	data = json.load(response)   
	print 

	line = text_spl[1].lower()

	for x in data:
		if x["id"]==line:
			send_text.text(number, ["lineStatuses"][0]["statusSeverityDescription"])
	return



