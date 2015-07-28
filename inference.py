import help
import sessions
import tube
import send_text
import google
import server

content = content.lower()
spl_txt = content.split()
db_data = sessions.retrive_data(number)
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


def infer(number,message):
	#******************************************************
	#If you dare remove the commenting I will kill you Edo!
	#******************************************************
	#check to see whether any database vars exist (should ALWAYS run true)
	if number == db_phone: #check to see what operator we are using as defined in 'operator'

		if (operator == None) and (db_phone == number):
			#now check to see what existing fields have been written to
			if (db_origin == None) and (db_destination != None): 
				#if there is nothing in origin and we have a dest for this number
				#take the origin that has been sent and add to db, then google
			if (db_origin != None) and (db_destination == None): #if we have origin but no destination
				#take the dest that has been sent and add to db, then google
			if (db_origin == None) and (db_destination == None): #neither have been populated, we assume starting with origin
				#take the origin, explain decision and ask for destination
		if operator == 'to':
			#we have a destination 
			#write to the database
			if (db_origin != None) and (db_destination != None):
				#Google
			else 
				#prompt for origin 
		if operator == 'from':
			#we have an origin 
			#write it to the db
			if (db_origin != None) and (db_destination != None):
				#Google
			else
				#prompt for destination
	else:
		send_text.text(number,'Your message is not valid and we cannot proccess it.')
	