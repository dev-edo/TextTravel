import help
import sessions
import send_text
import google

def infer(number,message,spl_txt,db_data):

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
    print operator
    print "-- operator"
    print db_phone
    print "-- phone on db"
    print db_origin
    print "-- origin on db"
    print db_destination
    print "-- dest on db"
    #******************************************************
    #Do NOT remove the commenting!
    #******************************************************
    #check to see whether any database vars exist (should ALWAYS run true)
    if number == db_phone: #check to see what operator we are using as defined in 'operator'

        if (operator == None) and (db_phone == number):
            #now check to see what existing fields have been written to
            if (db_origin == None) and (db_destination != None): 
                #if there is nothing in origin and we have a dest for this number
                #take the origin that has been sent and add to db, then google
                sessions.add_origin(number, message)
                step_details = google.directions(db_origin, db_destination)
                send_text.text(number,step_details)
                return

            elif (db_origin != None) and (db_destination == None):
                #if we have origin but no destination
                #take the dest that has been sent and add to db, then google
                sessions.add_destination(number, message)
                step_details = google.directions(db_origin, db_destination)
                send_text.text(number,step_details)
                return
            elif (db_origin == None) and (db_destination == None): #neither have been populated, we assume starting with origin
                #take the origin, explain decision and ask for destination
                sessions.add_origin(number, message)
                return "We have taken your last text as your origin, please send us your desired destination"
        if operator == 'to':
            #we have a destination 
            #write to the database
            sessions.add_destination(number, spl_txt[1:])
            if (db_origin != None) and (db_destination != None):
                step_details = google.directions(db_origin, db_destination)
                send_text.text(number,step_details)
                return
                #Google
            else: 
                #prompt for origin
                return "Where is the start point of your journey?" 

        if operator == 'from':
            #we have an origin 
            #write it to the db
            sessions.add_origin(number, spl_txt[1:])
            if (db_origin != None) and (db_destination != None):
                #Google
                step_details = google.directions(db_origin, db_destination)
                send_text.text(number,step_details)
                return
            else:
                #prompt for destination
                return "Where is the destination of your journey? "
    else:
        send_text.text(number,'Your message is not valid and we cannot proccess it.')

