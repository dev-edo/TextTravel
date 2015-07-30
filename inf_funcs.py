import google
import send_text
import sessions
def retrive_db(number):
    db_data = sessions.retrive_data(number)
    db_phone = db_data[0]
    db_origin = db_data[1]
    db_destination = db_data[2]
    return

def error(number):
    retrive_db(number)
    send_text.text(number, 'A fatal error occurred handling your request')
    return

def google_it(number, origin, destination):
    retrive_db(number)
    print "Google_it called"
    print "Origin is: "+str(origin)+". Type is "+str(type(origin))
    print "Destination is: "+str(destination)+". Type is "+str(type(destination))
    step_details = google.directions(origin, destination)  #TODO: make function
    print "step_details is: "+str(step_details)+". Type is "+str(type(step_details))
    for step in step_details:
        send_text.text(number,step)
    sessions.delete(number)
    return

def origin_plz(number):
    retrive_db(number)
    send_text.text(number, 'Where is the start point of your journey?')
    return

def dest_plz(number):
    retrive_db(number)
    send_text.text(number, 'Where is the end point of your journey?')
    return

def add_dest_google(number,message, origin, destination):
    retrive_db(number)
    sessions.add_destination(number, message)
    google_it(number, origin, destination)
    return

def add_org_google(number,message, origin, destination):
    retrive_db(number)
    sessions.add_origin(number, message)      #TODO: make function
    google_it(number, origin, destination)
    return

def inf_org(number,message):
    retrive_db(number)
    sessions.add_origin(number, message)   
    send_text.text(number, 'We have taken your last text as your origin; please send us your desired destination')
    return