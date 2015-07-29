import google
import send_text
import sessions

db_data = sessions.retrive_data(number)
db_phone = db_data[0]
db_origin = db_data[1]
db_destination = db_data[2]

def error(number):
	send_text.text('A fatal error occurred handling your request')
	return

def google_it(number):
	step_details = google.directions(db_origin, db_destination)  #TODO: make function
    send_text.text(number,step_details)
    return

def origin_plz(number):
	send_text.text(number, 'Where is the start point of your journey?')
	return

def dest_plz(number):
	send_text.text(number, 'Where is the end point of your journey?')
	return

def add_dest_google(number,message):
	sessions.add_destination(number, message)
    step_details = google.directions(db_origin, db_destination)
    send_text.text(number,step_details)
    return

def add_org_google(number,message):
	sessions.add_origin(number, message)      #TODO: make function
    step_details = google.directions(db_origin, db_destination)
    send_text.text(number,step_details)
    return

def inf_org(number,message):
	sessions.add_origin(number, message)   
    send_text.text(number, 'We have taken your last text as your origin; please send us your desired destination')
    return