from session import SessionStore
from copy import copy


class InMemorySessionStore(SessionStore):
    """An in-memory implementation of a SessionStore."""

    _map = {}

    def storeSession(self, session):
        assert session != None
        self._map[session.phoneNumber] = copy(session)

    def clearSession(self, mobile_number):
        assert phoneNumber != None
        self._map[phoneNumber] = None

    def retrieveSession(self, mobile_number):
        assert phoneNumber != None
        session = self._map[phoneNumber]
        if (session != None):
            session = copy(session)
        return session
