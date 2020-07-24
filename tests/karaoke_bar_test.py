import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.karaoke_bar import KaraokeBar


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.bar = KaraokeBar("CodeClanCaraoke")
        self.song = Song("Don't Stop Believin'", "Journey")
        self.songs_list = [
            Song("Africa", "Toto"),
            Song("Don't Stop Believin'", "Journey"),
            Song("Wonderwall", "Oasis"),
            Song("Uptown Girl", "Billy Joel"),
            Song("Ring of Fire", "Johnny Cash")
        ]

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

    # karaoke bar needs to make playlists for rooms
    def test_can_make_5_song_playlist_for_room(self):
        expected = 5
        actual = len(self.bar.make_playlist(self.bar.songs))
        self.assertEqual(expected, actual)

    def test_make_playlist_returns_list_of_songs(self):
        playlist = self.bar.make_playlist(self.bar.songs)
        expected = True
        actual = hasattr(playlist[0], "title")
        self.assertEqual(expected, actual)

    def test_playlist_is_random_order(self):
        expected = self.songs_list
        actual = self.bar.make_playlist(self.bar.songs)
        # combined = self.assertNotEqual(expected[0].title, actual[0].title) and self.assertNotEqual(expected[0].title, actual[0].title)
        index0 = expected[0].title == actual[0].title
        index1 = expected[1].title == actual[1].title
        self.assertFalse(index0 and index1)