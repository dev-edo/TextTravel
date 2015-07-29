import helpx
import sessions
import send_text
import google
import inf_funcs

def infer(number,message,spl_txt,db_data):

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

        number = long(number)
        db_phone = long(db_phone)
        sep = " "
        new_msg = sep.join(spl_txt)

        operator = spl_txt[0]
        print operator
        print "-- operator"
        print db_phone
        print "-- phone on db"
        print db_origin
        print "-- origin on db"
        print db_destination    
        print "-- dest on db"


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
            #edo's return function
            return response_body
        else:
          route(number,content,spl_txt,db_data)
        #******************************************************
        #Do NOT remove the commenting!
        #******************************************************

        #check to see what operator we are using as defined in 'operator'
        def route(number,message,spl_txt,db_data):
            if operator == None:
                #now check to see what existing fields have been written to
                if (db_origin != None) and (db_destination == None):
                    #if we have origin but no destination
                    #take the dest that has been sent and add to db, then google
                    inf_funcs.add_dest_google(number,message)
                    return
                elif (db_origin == None) and (db_destination != None): 
                    #if there is nothing in origin and we have a dest for this number
                    #take the origin that has been sent and add to db, then google
                    inf_funcs.add_org_google(number,message)
                    return

                elif (db_origin == None) and (db_destination == None): #neither have been populated, we assume starting with origin
                    #take the origin, explain decision and ask for destination
                    inf_funcs.inf_org(number,message)
                    return
            elif operator == 'to':
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
                #swap stored values around, and run google function
                inf_funcs.google_it(number, db_destination, db_origin)
                return
            else:
                inf_funcs.error(number)
                return
