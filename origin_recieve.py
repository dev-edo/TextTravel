import send_text, sessions
def origin(number,origin):
	#Stuff to store the number and origin
	send_text.text(number, 'Now the destination please?')
	sessions.add_origin(number, origin)
	return
