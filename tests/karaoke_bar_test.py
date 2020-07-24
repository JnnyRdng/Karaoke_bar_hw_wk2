import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.karaoke_bar import KaraokeBar


class TestKaraokeBar(unittest.TestCase):
    def test_karaoke_bar_has_name(self):
        kbar = KaraokeBar("CodeClanCaraoke")
        expected = "CodeClanCaraoke"
        actual = kbar.name
        self.assertEqual(expected, actual)

    def test_karaoke_bar_has_guests(self):
        kbar = KaraokeBar("CodeClanCaraoke")
        expected = 6
        actual = len(kbar.guests)
        self.assertEqual(expected, actual)