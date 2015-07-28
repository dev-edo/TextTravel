import config

def text( number,message ): 
	from clockwork import clockwork
 
	api = clockwork.API(config.key)
 
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
