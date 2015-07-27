import send_text
import urllib2
import json

line = raw_input('Enter Tube line:')

response = urllib2.urlopen('https://api.tfl.gov.uk/line/mode/tube/status')
data = json.load(response)   
print 

line.lower()


for line in data[id]:
<<<<<<< HEAD
	print str(line)
	

=======
	print line
>>>>>>> 565fd25f09a4aad35a5b5ee3907bb2ae50e46673
