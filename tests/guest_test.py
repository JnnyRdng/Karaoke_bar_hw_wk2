import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def test_can_make_a_guest_with_name(self):
        guest = Guest("Rick")
        expected = "Rick"
        actual = guest.name
        self.assertEqual(expected, actual)