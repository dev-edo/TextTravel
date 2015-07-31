# traxt.

YRS2015 Project using the ClockworkSMS and Google APIs.

traxt. allows users to recieve directions through SMS, instead of through their data plan. This is useful for tourists who either have no data, or who are using a cheap phone which doesn't have access to the internet. This is alos great for people who have used up their data and need directions quickly. 

At first, the user sends a message to our number. The user's number and their message is passed on from Clockwork to our **server.py**. server.py thenextracts the data from Clockwork. It then checks whether their number is already stored in our database. If it is, the user's information is passed on to the **interface.py** file. If their number is not stored, it stores it, before moving on to the interface.py file. 

The interface.py spilts their message, checking whether they 
