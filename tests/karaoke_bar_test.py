import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.karaoke_bar import KaraokeBar


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.bar = KaraokeBar("CodeClanCaraoke")

    def test_karaoke_bar_has_name(self):
        expected = "CodeClanCaraoke"
        actual = self.bar.name
        self.assertEqual(expected, actual)

    def test_karaoke_bar_has_guests(self):
        expected = 6
        actual = len(self.bar.guests)
        self.assertEqual(expected, actual)

    def test_karaoke_bar_has_songs(self):
        expected = 8
        actual = len(self.bar.songs)
        self.assertEqual(expected, actual)

    def test_karaoke_bar_first_song_is_Africa_by_Toto(self):
        self.assertEqual("Africa", self.bar.songs[0].title)
        self.assertEqual("Toto", self.bar.songs[0].artist)

    def test_karaoke_bar_third_song_is_Wonderwall_by_Oasis(self):
        self.assertEqual("Wonderwall", self.bar.songs[2].title)
        self.assertEqual("Oasis", self.bar.songs[2].artist)

    def test_karaoke_bar_has_two_rooms(self):
        expected = 2
        actual = len(self.bar.rooms)
        self.assertEqual(expected, actual)

    def test_karaoke_bar_has_two_empty_room_objects(self):
        expected = []
        actual = self.bar.rooms[0].guests
        self.assertEqual(expected, actual)
