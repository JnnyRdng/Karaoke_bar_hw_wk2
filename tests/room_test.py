import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()
        self.songs = [
            Song("Africa", "Toto"),
            Song("Don't Stop Believin'", "Journey"),
            Song("Wonderwall", "Oasis"),
            Song("Uptown Girl", "Billy Joel"),
            Song("Ring of Fire", "Johnny Cash"),
        ]
        self.guest = Guest("Timmy")

    def test_empty_room_has_no_guests(self):
        expected = []
        actual = self.room.guests
        self.assertEqual(expected, actual)

    def test_empty_room_has_no_songs(self):
        expected = []
        actual = self.room.playlist
        self.assertEqual(expected, actual)

    def test_set_playlist_for_room__get_length(self):
        self.room.start_playlist(self.songs)
        expected = 5
        actual = len(self.room.playlist)
        self.assertEqual(expected, actual)

    def test_playlist_items_are_song_objects(self):
        self.room.start_playlist(self.songs)
        expected = "Uptown Girl"
        actual = self.room.playlist[3].title
        self.assertEqual(expected, actual)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        expected = 1
        actual = len(self.room.guests)
        self.assertEqual(expected, actual)

    def test_add_guest_to_room_adds_guest_object(self):
        self.room.add_guest_to_room(self.guest)
        expected = "Timmy"
        actual = self.room.guests[0].name
        self.assertEqual(expected, actual)
