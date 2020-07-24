import unittest

from src.song import Song


class TestSong(unittest.TestCase):
    def test_song_has_title(self):
        song = Song("Deep Blue", "Arcade Fire")
        expected = "Deep Blue"
        actual = song.title
        self.assertEqual(expected, actual)

    def test_song_has_an_artist(self):
        song = Song("Deep Blue", "Arcade Fire")
        expected = "Arcade Fire"
        actual = song.artist
        self.assertEqual(expected, actual)
