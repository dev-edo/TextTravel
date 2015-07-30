import help
import sessions
import send_text
import google
import inf_funcs
import tube
import bus

def infer(number,message,spl_txt,db_data):
    print "AM I RUNNING JACOB?!??!  "
    if db_data != None:
        print "1"
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
        print "2"
    else: 
        print "3"
        sessions.insert(number)
        db_data = sessions.retrive_data(number)
        db_phone = db_data[0]
        db_origin = db_data[1]
        db_destination = db_data[2]
        print "4"

    number = long(number)
    print "5"
    db_phone = long(db_phone)
    print "6"
    sep = " "
    print "7"
    new_msg = sep.join(spl_txt)
    print "8"
    operator = spl_txt[0]
    print operator
    print "-- operator"
    print db_phone
    print "-- phone on db"
    print db_origin
    print "-- origin on db"
    print db_destination    
    print "-- dest on db"
    print "9"

    if operator == 'tube':
        print "10"
        item = spl_txt[1]
        tube.tube(number, spl_txt[1])
        print "11"
        return response_body

    elif operator == 'help':
        print "12"
        send_text.text(number,'To get tube status, "tube {line}", for route info, "to {place}" and "from {place}"')
        return response_body
    elif operator == 'bus':
        print "13"
        item = spl_txt[1]
        bus.bus(number, item)
        return response_body
    else:
        print "14"
        route(number,message,spl_txt,db_data, operator)
        print "15"
        #******************************************************
        #Do NOT remove the commenting!
        #******************************************************

#check to see what operator we are using as defined in 'operator'
def route(number,message,spl_txt,db_data, operator):
    sep = " "
    new_msg = sep.join(spl_txt)
    db_phone = db_data[0]
    db_origin = db_data[1]
    db_destination = db_data[2]
    print "16"
    if operator == None:
        #now check to see what existing fields have been written to
        print "17"
        if (db_origin != None) and (db_destination == None):
            print "a"
            #if we have origin but no destination
            #take the dest that has been sent and add to db, then google
            print "b"
            inf_funcs.add_dest_google(number,message)
            print "c"
            return
        elif (db_origin == None) and (db_destination != None): 
            print "d"
            #if there is nothing in origin and we have a dest for this number
            #take the origin that has been sent and add to db, then google
            inf_funcs.add_org_google(number,message)
            print "e"
            return

        elif (db_origin == None) and (db_destination == None): #neither have been populated, we assume starting with origin
            #take the origin, explain decision and ask for destination
            print "f"
            inf_funcs.inf_org(number,message)
            print "g"
            return
    elif operator == 'to':
        print "18"
        #we have a destination 
        #write to the database
        sessions.add_destination(number, new_msg)
        if (db_origin != None) and (db_destination != None):
            inf_funcs.google_it(number)
            return
        elif (db_origin != None) and (db_destination == None):
            inf_funcs.dest_plz
            return
        else: 
            inf_funcs.origin_plz
            return

    elif operator == 'from':
        print "19"
        #we have an origin 
        #write it to the db
        sessions.add_origin(number, new_msg)
        if (db_origin != None) and (db_destination != None):  #TODO: update if
            inf_funcs.google_it(number)
            return
        elif (db_origin == None) and (db_destination != None):  #TODO: update if
            inf_funcs.origin_plz
            return
    elif (operator == 'return') and (db_origin != None) and (db_destination != None):
        print "20"
        #swap stored values around, and run google function
        inf_funcs.google_it(number, db_destination, db_origin)
        return
    else:
        print "21"
        inf_funcs.error(number)
        return
