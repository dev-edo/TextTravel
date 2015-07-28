from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import help
import sessions
import origin_recieve
import destination_recieve
import tube
import send_text
import google
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
      db_phone = db_data[0]
      db_origin = db_data[1]
      db_destination = db_data[2]
    
    operator = spl_txt[0]
    item = spl_txt[1]

    print spl_txt[0]

    print spl_txt

    if operator == 'tube':
        tube.tube(number, spl_txt)
        return response_body

    if operator == 'help':
        send_text.text(number,'To get tube status, "tube {line}", for route info, "to {place}" and "from {place}"')
        return response_body

    
        #make a sesson
    if operator == 'to':
      if db_phone == None:
        sessions.insert(number)

        if (db_origin != None) and (db_destination != None):
          routes = google.google(db_origin,db_destination)
          routes = routes.join()
          send_text.text(number, routes)
          return response_body
        else:
          sessions.add_destination(number, item)
        if db_destination == None:
          send_text.text(number, 'Origin now please')
        else: 
          routes = google.google(db_origin,db_destination)
          routes = routes.join()
          send_text.text(number, routes)
          return response_body
      else:
          if (db_origin != None) and (db_destination != None):
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
            pass
          else:
            if db_origin == None:
              send_text.text(number, 'Origin now please')
            else: 
              routes = google.google(db_origin,db_destination)
              routes = routes.join()
              send_text.text(number, routes)
              return response_body
              pass
    if (operator == 'from'):
        if db_phone == None:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None):
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
            
          else:
            sessions.add_origin(number, item)
          if db_destination == None:
            send_text.text(number, 'Destination now please')
          else: 
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
        else:
          if (db_origin != None) and (db_destination != None):
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
          else:
            if db_destination == None:
              send_text.text(number, 'Destination now please')
            else: 
              routes = google.google(db_origin,db_destination)
              routes = routes.join()
              send_text.text(number, routes)
              return response_body

    elif (db_origin != None):
      if db_phone == None:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None):
            routes = google.google(db_origin, db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
            
          else:
            sessions.add_destination(number, item)
          if db_destination == None:
            send_text.text(number, 'Destination now please')
          else: 
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
      else:
        if (db_origin != None) and (db_destination != None):
          routes = google.google(db_origin,db_destination)
          routes = routes.join()
          send_text.text(number, routes)
          return response_body
        else:
          if db_origin == None:
            send_text.text(number, 'Origin now please')
          else: 
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
    elif (db_destination != None):
      if db_phone == None:
          sessions.insert(number)

          if (db_origin != None) and (db_destination != None):
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
          else:
            sessions.add_origin(number, item)
          if db_destination == None:
            send_text.text(number, 'Destination now please')
          else: 
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
      else:
        if (db_origin != None) and (db_destination != None):
          routes = google.google(db_origin,db_destination)
          routes = routes.join()
          send_text.text(number, routes)
          return response_body
        else:
          if db_destination == None:
            send_text.text(number, 'Destination now please')
          else: 
            routes = google.google(db_origin,db_destination)
            routes = routes.join()
            send_text.text(number, routes)
            return response_body
    
    return response_body



httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   texttravel # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.serve_forever()

