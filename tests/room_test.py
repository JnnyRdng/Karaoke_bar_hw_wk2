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
        self.guest = Guest("Timmy", 20)
        self.guest_not_in_room = Guest("Jimmy", 40)

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

    def test_guest_can_leave_a_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.remove_guest(self.guest)
        expected = 0
        actual = len(self.room.guests)
        self.assertEqual(expected, actual)

    def test_guest_can_leave_a_room__return(self):
        self.room.add_guest_to_room(self.guest)
        expected = True
        actual = self.room.remove_guest(self.guest)
        self.assertEqual(expected, actual)

    def test_is_guest_in_room(self):
        expected = False
        actual = self.room.is_guest_in_room(self.guest_not_in_room)
        self.assertEqual(expected, actual)

    def test_guest_cant_leave_room_theyre_not_in(self):
        self.room.add_guest_to_room(self.guest)
        expected = False
        actual = self.room.remove_guest(self.guest_not_in_room)
        self.assertEqual(expected, actual)

    def test_room_returns_guest_list(self):
        self.room.add_guest_to_room(self.guest)
        expected = [self.guest]
        actual = self.room.return_guest_list()
        self.assertEqual(expected, actual)

    #extensions
    def test_max_room_size_set(self):
        expected = 3
        actual = self.room.max_size
        self.assertEqual(expected, actual)

    def test_room_has_fewer_guests_than_max(self):
        expected = True
        actual = self.room.room_has_space()
        self.assertEqual(expected, actual)

    def test_room_has_more_guests_than_max(self):
        self.room.add_guest_to_room(Guest("Timmy", 20))
        self.room.add_guest_to_room(Guest("Timmy", 20))
        self.room.add_guest_to_room(Guest("Timmy", 20))
        self.room.add_guest_to_room(Guest("Timmy", 20))
        self.room.add_guest_to_room(Guest("Timmy", 20))
        expected = False
        actual = self.room.room_has_space()
        self.assertEqual(expected, actual)

    def test_room_cant_add_guests_past_max(self):
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        expected = 3
        actual = len(self.room.guests)
        self.assertEqual(expected, actual)

    def test_room_cant_add_guests_past_max__return_False(self):
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.room.add_guest_to_room(Guest("Jimmy", 40))
        expected = False
        actual = self.room.add_guest_to_room(Guest("Jimmy", 40))
        self.assertEqual(expected, actual)

    def test_room_has_entry_fee(self):
        expected = 10
        actual = self.room.entry_fee
        self.assertEqual(expected, actual)

    def test_guest_has_enough_money_to_enter(self):
        guest = Guest("Monty", 100)
        expected = True
        actual = self.room.enough_money(guest)
        self.assertEqual(expected, actual)