import unittest

from src.song import Song
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.empty_room = Room()
        self.songs = [
            Song("Africa", "Toto"),
            Song("Don't Stop Believin'", "Journey"),
            Song("Wonderwall", "Oasis"),
            Song("Uptown Girl", "Billy Joel"),
            Song("Ring of Fire", "Johnny Cash"),
        ]

    def test_empty_room_has_no_guests(self):
        expected = []
        actual = self.empty_room.guests
        self.assertEqual(expected, actual)

    def test_empty_room_has_no_songs(self):
        expected = []
        actual = self.empty_room.playlist
        self.assertEqual(expected, actual)

    def test_set_playlist_for_room__get_length(self):
        self.empty_room.start_playlist(self.songs)
        expected = 5
        actual = len(self.empty_room.playlist)
        self.assertEqual(expected, actual)

    def test_playlist_items_are_song_objects(self):
        self.empty_room.start_playlist(self.songs)
        expected = "Uptown Girl"
        actual = self.empty_room.playlist[3].title
        self.assertEqual(expected, actual)

