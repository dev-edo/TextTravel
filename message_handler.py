from persistence.session import Session
from messages.message import TextMessage


class MessageHandler:
    """Deals with receiving and responding to text messages."""

    def __init__(self, session_store, message_sender):
        assert session_store != None
        assert message_sender != None
        self._session_store = session_store
        self._message_sender = message_sender

    def handle_message(self, text_message):
        """Handles an incoming text message."""
        assert text_message != None
        mobile_number = text_message.mobile_number
        request_body = text_message.body
        session_store = self._session_store

        # Retrieve the session, making a new one if necessary.
        current_session = session_store.retrieve_session(mobile_number)
        if current_session == None:
            current_session = Session(mobile_number)

        # Calculate the response.
        (response_body, new_session) = self._process_message(request_body, current_session)

        # Persist the new session.
        if new_session == None:
            session_store.clear_session(mobile_number)
        else:
            session_store.store_session(new_session)

        # If there's a response to be sent, send it.
        if response_body != None:
            self._message_sender.send_message(TextMessage(mobile_number, response_body))

    def _process_message(self, request_body, session):
        """Given the request body text and the session, calculates the response and new session."""
        assert request_body != None
        assert session != None

        # TODO: Need to actually implement the logic here.
        return ("Stock response", session)
