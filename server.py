from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
import sessions
import tube
import send_text
import google
import inference
import bus
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
    if db_data != None:
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
    else: 
        sessions.insert(number)
        db_data = sessions.retrive_data(number)
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
    
    operator = spl_txt[0]
    
    inference.route(number,message,spl_txt,db_data)

<<<<<<< HEAD
=======
    

    if operator == 'tube':
        item = spl_txt[1]
        tube.tube(number, spl_txt[1])
        return response_body

    if operator == 'help':
        send_text.text(number,'To get tube status, "tube {line}", for route info, "to {place}" and "from {place}"')
        return response_body
    if operator == 'bus':
        item = spl_txt[1]
        bus.bus(number, item)
        return response_body
    if operator == 'return':
        pass
        inference.infer(number,content,spl_txt,db_data)
        return response_body
    else:
      inference.infer(number,content,spl_txt,db_data)

    
    
    
>>>>>>> 708fd602614e4553f0136fcfc39c44283013ab50
    return response_body



httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.serve_forever()

