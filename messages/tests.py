import unittest
from message import TextMessage


class SessionTests(unittest.TestCase):

    def test_construction(self):
        message = TextMessage(123, "body")
        self.assertEqual(123, message.mobile_number)
        self.assertEqual("body", message.body)
 
    def test_two_identical_messages_are_equal(self):
        message1 = TextMessage(123, "body")
        message2 = TextMessage(123, "body")
        self.assertEqual(message1, message2)

    def test_messages_with_different_mobile_numbers_are_not_equal(self):
        message1 = TextMessage(123, "body")
        message2 = TextMessage(456, "body")
        self.assertNotEqual(message1, message2)

    def test_messages_with_different_bodies_are_not_equal(self):
        message1 = TextMessage(123, "body")
        message2 = TextMessage(123, "foo")
        self.assertNotEqual(message1, message2)


if __name__ == '__main__':
    unittest.main()