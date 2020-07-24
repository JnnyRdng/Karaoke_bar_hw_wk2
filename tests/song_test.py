import unittest

from src.song import Song


class TestSong(unittest.TestCase):
    def test_song_has_title(self):
        song = Song("Deep Blue")
        expected = "Deep Blue"
        actual = song.title
        self.assertEqual(expected, actual)

