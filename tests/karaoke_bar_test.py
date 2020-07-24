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
        expected = 10
        actual = len(self.bar.songs)
        self.assertEqual(expected, actual)