from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
import sessions
import origin_recieve
import destination_recieve
import tube
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
    db_phone = db_data[0]
    db_origin = db_data[1]
    db_destination = db_data[2]
    spl_txt[0] = operator


    print spl_txt[0]

    print spl_txt

    if operator == 'tube':
        tube.tube(number, spl_txt)
        return response_body

    
        #make a sesson
    if operator == 'to':
        if db_phone != number:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None):
            #Google
            pass
          else:
            sessions.add_destination(number, db_destination)
          if db_destination == None:
            send_text.text(number, 'Origin now please')
          else: 
            #google
            pass
        else:
          if (db_origin != None) and (db_destination != None)
            #Google
          else:
            if db_origin == None:
              send_text.text(number, 'Origin now please')
            else: 
              #google
              pass
    if (operator == 'from'):
        if db_phone != number:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None)
            #Google
            pass
          else:
            sessions.add_origin(number, db_origin)
          if db_destination == None:
            send_text.text(number, 'Destination now please')
          else: 
            #google
            pass
        else:
          if (db_origin != None) and (db_destination != None)
            #Google
          else:
            if db_destination == None:
              send_text.text(number, 'Destination now please')
            else: 
              #google
              pass

    else if (db_origin != None):
      if db_phone != number:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None)
            #Google
            pass
          else:
            sessions.add_destination(number, db_destination)
          if db_destination == None:
            send_text.text(number, 'Origin now please')
          else: 
            #google
            pass
        else:
          if (db_origin != None) and (db_destination != None)
            #Google
          else:
            if db_origin == None:
              send_text.text(number, 'Origin now please')
            else: 
              #google
              pass   
    else if (db_destination != None):
        #store destination and check if both are filled
    else:
        #make an error
    return response_body

   

    return response_body



httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.serve_forever()

