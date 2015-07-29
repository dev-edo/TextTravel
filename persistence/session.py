

class Session:
    """Represents a session (or conversation) for a single phone number."""

    def __init__(self, mobile_number, origin = None, destination = None):
        assert mobile_number != None
        self._mobile_number = mobile_number
        self.origin = origin
        self.destination = destination

    @property
    def mobile_number(self):
        """The mobile phone number that uniquely identifies the session.
           This cannot be modified."""
        return self._mobile_number

    def __eq__(self, other):
        return other != None and \
               self.mobile_number == other.mobile_number and \
               self.origin == other.origin and \
               self.destination == other.destination

    def __repr__(self):
        return "Session(mobile_number: {}, origin: {}, destination: {})".format(
            self.mobile_number, self.origin, self.destination)


class SessionStore:
    """Encapsulates the persistence and retrieval of the state of a session,
       on a per-mobile number basis."""

    def store_session(self, session):
        """Persists the specified session in the store, overwriting any existing
           session with the mobile number."""
        raise NotImplementedError("Subclass must implement abstract method")

    def clear_session(self, mobile_number):
        """Removes any session with the specified mobile number from the store."""
        raise NotImplementedError("Subclass must implement abstract method")

    def retrieve_session(self, mobile_number):
        """Retrieves a session form the store with the specified mobile number.
           returns None if there is no such session in the store."""
        raise NotImplementedError("Subclass must implement abstract method")
