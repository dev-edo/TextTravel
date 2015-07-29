from session import SessionStore
from copy import copy


class InMemorySessionStore(SessionStore):
    """An in-memory implementation of a SessionStore."""

    def __init__(self):
        self._map = {}

    def store_session(self, session):
        assert session != None
        self._map[session.mobile_number] = copy(session)

    def clear_session(self, mobile_number):
        assert mobile_number != None
        self._map[mobile_number] = None

    def retrieve_session(self, mobile_number):
        assert mobile_number != None
        if mobile_number in self._map:
            return copy(self._map[mobile_number])
        return None
