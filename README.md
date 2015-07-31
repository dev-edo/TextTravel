# traxt.

YRS2015 Project using the ClockworkSMS and Google APIs.

traxt. allows users to recieve directions through SMS, instead of through their data plan. This is useful for tourists who either have no data, or who are using a cheap phone which doesn't have access to the internet. This is alos great for people who have used up their data and need directions quickly. 

At first, the user sends a message to our number. The user's number and their message is passed on from Clockwork to our **server.py**. server.py thenextracts the data from Clockwork. It then checks whether their number is already stored in our database. If it is, the user's information is passed on to the **interface.py** file. If their number is not stored, it stores it, before moving on to the interface.py file. 

The interface.py spilts their message, checking the content of the user's message, and sending them the necessary information. It does this by interacting with **tube.py**, **bus.py**, **google.py**, and of course, **send_text.py**. 

google.py
---------

google.py uses the *Google Directions API* to generate an XML file containing all the steps of the journey. This then returns the directions as a string. The interface.py file calls this function. 

bus.py and tube.py
------------------

Both bus.py and tube.py use the *Transport for London* API to generate a JSON file. This is converted into a readable string, and is send to the user, giving them up to date bus and tube status. Both are simple to use, and are called within the interface.py file. 

send_text.py
------------

The send_text.py file uses the *Clockwork SMS* API. It calls the API, passing it a message, and the user's number

--------------------------------------------------------------------

To start using traxt. 
