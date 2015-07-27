from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
def texttravel(environ, start_response):
    response_body = ""

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    d = parse_qs(environ['QUERY_STRING'])
    content = d.get('content', [''])[0] 
    from_sender = d.get('from', [''])[0]
    help.help(from_sender)

    return response_body



httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.serve_forever()

