import send_text
import sessions


def help( number ): 
	message = 'Text me your origin to get started'
	send_text.text(number,message)
	sessions.insert(number)
	return
