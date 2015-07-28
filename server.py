from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
import sessions
import origin_recieve
#import destination_recieve
import tube2
def texttravel(environ, start_response):
    response_body = ""

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    d = parse_qs(environ['QUERY_STRING'])
    content = d.get('content', [''])[0] 
    from_sender = d.get('from', [''])[0]
    number = from_sender


    content = content.lower()
    spl_txt = content.split()
    db_data = sessions.retrive_data(number)

    if spl_txt[0] == 'tube':
        tube2.tube(number, spl_txt)
        return response_body

    if content == "help" or db_data == None:
        help.help(from_sender)
        return response_body

    if (db_data[1] == None) and (db_data[2] == None):
        origin_recieve.origin(number, content)
        return response_body

    if (db_data[1] != None) and (db_data[2] == None):
        destination_recieve.destination(number, content)
        return response_body

        return response_body



httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.serve_forever()

