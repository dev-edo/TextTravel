import sessions, send_text, google, time

def process(mobile, message):
    # extract the first word, and call it "operator"
    message_array = message.split()
    operator      = message_array[0]
    data          = sessions.retrive_data(mobile)
    origin        = data[1]
    destination   = data[2]
    #Is the operator "from"
    if operator == "from":
        #do we have a stored destination?
        if destination != None:
            #google using the rest of the message and the stored destination
            google_it(mobile, " ".join(message_array[1:]), destination)
        # else:
        else:
            # save the rest of the message as the origin
            origin = " ".join(message_array[1:])
            sessions.add_origin(mobile, origin)
            # Request the destination
            dest_req(mobile)

    #ok, how about "to"
    elif operator == "to":
        process_origin(mobile, " ".join(message_array[1:]), origin, destination)
    #if they have asked to reset:
    elif operator == "reset":
        sessions.delete(mobile)
        send_text.text(mobile, "Reset successful!")
    # so we don't know the operator.
    else:
        # Do we have a saved origin?
        if origin != None:
            # then this must be the destination
            destnation = " ".join(message_array)
            # google using the saved origin and the rest of the message
            print "Origin is: "     +str(origin)     +". Type is "+str(type(origin))
            print "Destination is: "+str(destination)+". Type is "+str(type(destination))
            google_it(mobile, origin, destination)
        # we dont have a saved origin, so this must be it
        else:
            # save the message as the origin
            origin = " ".join(message_array)
            sessions.add_origin(mobile, origin)
            # prompt for the destination
            dest_req(mobile)

def google_it(mobile, origin, destination):
    #print "Google_it called"
    #print "Origin is: "+str(origin)+". Type is "+str(type(origin))
    #print "Destination is: "+str(destination)+". Type is "+str(type(destination))
    step_details = google.directions(origin, destination)  #TODO: make function
    #print "step_details is: "+str(step_details)+". Type is "+str(type(step_details))
    if step_details == []:
        send_text.text(mobile, "Unfourtunatley, we cannot find directions for you. Sorry for any inconvinience caused.")
    else:
        i = 1
        for step in step_details:
            send_text.text(mobile, str(i) + ") " + step)
            i += 1
            time.sleep(3)
    sessions.delete(mobile)
    return

def dest_req(mobile):
    send_text.text(mobile, 'Where is the end point of your journey?')
    return

def origin_req(mobile):
    send_text.text(mobile, 'Where is the start point of your journey?')
    return

def process_origin(mobile, message_array, origin, destination):
    # do we have a stored origin
    if origin != None:
        # google using the stored origin and the rest of the message
        google_it(mobile, origin, message_array[1:])
    # else:
    else:
        # save the rest of the message as the destination
        destination = message_array[1:]
        sessions.add_destination(mobile, destination)
        # Request the origin
        origin_req(mobile)