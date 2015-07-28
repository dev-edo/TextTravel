import unittest
from session import Session


class SessionTests(unittest.TestCase):

    def test_two_identical_sessions_are_equal(self):
        session1 = Session(123)
        session1.destination = "end"
        session1.origin = "start"

        session2 = Session(123)
        session2.destination = "end"
        session2.origin = "start"

        self.assertEqual(session1, session2)

    def test_two_different_sessions_are_not_equal(self):
        session1 = Session(123)
        session1.destination = "end"
        session1.origin = "start"

        session2 = Session(456)
        session2.destination = "end"
        session2.origin = "start"

        self.assertNotEqual(session1, session2)


class MemorySessionTests(unittest.TestCase):



if __name__ == '__main__':
    unittest.main()