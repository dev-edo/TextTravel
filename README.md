# traxt.

YRS2015 Project using the ClockworkSMS and Google APIs.

Traxt is a SMS based API service which allows users to access various information modules via a single number. The system is fully modular and allows developers to add/remove features to the API with ease and simplicity. Requests are intrepreted by the service module which passes on the data to the relevent module after natural language processing determines the function. 

At first, the user sends a message to our number. The user's number and their message is passed on from Clockwork to our **server.py**. server.py then extracts the data from Clockwork. We then check whether a session exists for that user and if not we create one by default. This is the passed to **interface.py**. 

**interface.py** spilts their message, checking the content of the user's message, and sending them the necessary information. It does this by interacting with **tube.py**, **bus.py**, **google.py**, and of course, **send_text.py**. 

google.py
---------

google.py uses the *Google Directions API* to generate an XML file containing all the steps of the journey. This then returns the directions as a string. The interface.py file calls this function. 

bus.py and tube.py
------------------

Both bus.py and tube.py use the *Transport for London* API to generate a JSON file. This is converted into a readable string, and is send to the user, giving them up to date bus and tube status. Both are simple to use, and are called within the interface.py file. 

send_text.py
------------

The **send_text.py** file uses the *Clockwork SMS* API. It calls the API, passing it a message, and the user's number. This underpins the whole service and is uavilable for all modules to use. 

--------------------------------------------------------------------

To start using traxt. 
---------------------

Text "help" to the secret number that will appear after YRS presentations. 
