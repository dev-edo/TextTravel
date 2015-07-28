import urllib2
import json

line = raw_input('Enter Tube line:')

response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
data = json.load(response)   
print 

line = line.lower()

for x in data:
	if x["id"]==line:
		print x["name"]
		#print x["modified"][11:19]
		print x["lineStatuses"][0]["statusSeverityDescription"]
