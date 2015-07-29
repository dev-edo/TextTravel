from message import MessageSender


class ConsoleMessageSender(MessageSender):
    """Implementation of MessageSender that simply logs to the console."""

    def send_message(self, text_message):
        """Sends a text message to its associated mobile number."""
        print ("    {} <-- {}".format(text_message.mobile_number, text_message.body))

