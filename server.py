from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
import sessions
import tube
import send_text
import google
import interface
import bus

print "Server Restarted"

def texttravel(environ, start_response):
    response_body = ""
    #print "1"
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    #print "2"
    d = parse_qs(environ['QUERY_STRING'])
    content = d.get('content', [''])[0] 
    from_sender = d.get('from', [''])[0]
    number = from_sender
    print content, number
    #print "3"


    content = content.lower()
    spl_txt = content.split()
    db_data = sessions.retrive_data(number)
    if db_data != None:
        #print "4"
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
        #print "5"
    else: 
        #print "6"
        sessions.insert(number)
        db_data = sessions.retrive_data(number)
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
        #print "7"
    
    operator = spl_txt[0]
    #print "8"
    interface.process(number,content)
    #print "9"
    return response_body


#print "a"
httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )
#print "b"
# Wait for a single request, serve it and quit.
httpd.serve_forever()
#print "c"