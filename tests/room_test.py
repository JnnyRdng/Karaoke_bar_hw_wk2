import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def test_room_has_no_guests(self):
        room = Room()
        expected = []
        actual = room.guests
        self.assertEqual(expected, actual)