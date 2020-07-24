import unittest

from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.empty_room = Room()

    def test_empty_room_has_no_guests(self):
        expected = []
        actual = self.empty_room.guests
        self.assertEqual(expected, actual)

    def test_empty_room_has_no_songs(self):
        expected = []
        actual = self.empty_room.playlist
        self.assertEqual(expected, actual)

