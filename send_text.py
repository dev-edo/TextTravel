def text( number,message ): 
	from clockwork import clockwork
 
	api = clockwork.API('bc7209eb2eb0c99f74d7a96c03043f5271284866')
 
	message = clockwork.SMS(
	    to = number, 
	    message = message)
 
	response = api.send(message)
 
	if response.success:
    		print (response.id)
	else:
	    print (response.error_code)
	    print (response.error_description)
	return

text(number,message);