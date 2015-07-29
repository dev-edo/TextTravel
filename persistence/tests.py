import unittest
from session import Session
from memorysession import InMemorySessionStore


class SessionTests(unittest.TestCase):

    def test_construction(self):
        session = Session(123, "start", "end")
        self.assertEqual(123, session.mobile_number)
        self.assertEqual("start", session.origin)
        self.assertEqual("end", session.destination)

    def test_two_identical_sessions_are_equal(self):
        session1 = Session(123, "start", "end")
        session2 = Session(123, "start", "end")
        self.assertEqual(session1, session2)

    def test_sessions_with_different_mobile_numbers_are_not_equal(self):
        session1 = Session(123, "start", "end")
        session2 = Session(456, "start", "end")
        self.assertNotEqual(session1, session2)

    def test_sessions_with_different_origins_are_not_equal(self):
        session1 = Session(123, "start", "end")
        session2 = Session(123, "foo", "end")
        self.assertNotEqual(session1, session2)

    def test_sessions_with_different_destinations_are_not_equal(self):
        session1 = Session(123, "start", "end")
        session2 = Session(123, "start", "foo")
        self.assertNotEqual(session1, session2)


class MemorySessionTests(unittest.TestCase):

    def test_retrieve_session_on_an_empty_store_returns_none(self):
        store = InMemorySessionStore()
        session = store.retrieve_session(123)
        self.assertIsNone(session)

    def test_store_and_retrieve_a_session(self):
        store = InMemorySessionStore()
        session1 = Session(123)
        store.store_session(session1)
        session2 = store.retrieve_session(123);
        self.assertEqual(session1, session2)

    def test_retrieve_an_updated_session(self):
        store = InMemorySessionStore()
        session1 = Session(123, "start", "end")
        store.store_session(session1)
        session2 = Session(123, "foo", "bar")
        store.store_session(session2);
        session3 = store.retrieve_session(123);
        self.assertEqual(session2, session3)


if __name__ == '__main__':
    unittest.main()