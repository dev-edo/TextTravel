import send_text
import sessions



def help(number): 
	db_data = sessions.retrive_data(number)

	message = 'Text me your origin to get started'
	send_text.text(number, message)
	if number == db_data[0]:
		pass
	else:
		sessions.insert(number)

	return
