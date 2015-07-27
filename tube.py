import send_text
import urllib2
import json

line = raw_input('Enter Tube line:')

response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
data = json.load(response)   
print data