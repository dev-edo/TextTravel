from message_handler import MessageHandler
from persistence.memory import InMemorySessionStore 
from messages.console import ConsoleMessageSender
from messages.message import TextMessage
import re

if __name__ == '__main__':

    session_store = InMemorySessionStore()
    message_sender = ConsoleMessageSender()
    message_handler = MessageHandler(session_store, message_sender)

    pattern = re.compile(r"^[\d ]+$")
    mobile_number = None
    while True:
        line = raw_input().strip()

        # Quit if requested.
        if line == "quit" or line == "q":
            break

        # Try to parse a mobile number
        if pattern.match(line):
            mobile_number = line
            print("Mobile number set to {}".format(mobile_number))

        # Otherwise if we have a message body and a number, create atext message and handle it.
        elif line != "" and mobile_number != None:
            print("    {} --> {}".format(mobile_number, line))
            text_message = TextMessage(mobile_number, line)
            message_handler.handle_message(text_message)
