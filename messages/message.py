class TextMessage:
    """Represents a text message, consisting of a phone number and a message body."""

    def __init__(self, mobile_number, body):
        assert mobile_number != None
        assert body != None
        self._mobile_number = mobile_number
        self._body = body

    @property
    def mobile_number(self):
        """The mobile number associated with the text message."""
        return self._mobile_number

    @property
    def body(self):
        """The text body associated with the text message."""
        return self._body

    def __eq__(self, other):
        return other != None and \
               self.mobile_number == other.mobile_number and \
               self.body == other.body

    def __repr__(self):
        return "TextMessage(mobile_number: {}, body: {})".format(
            self.mobile_number, self.body)


class MessageSender:
    """Encapsulates the function of sending a text message."""

    def send_message(self, text_message):
        """Sends a text message to its associated mobile number."""
        raise NotImplementedError("Subclass must implement abstract method")
