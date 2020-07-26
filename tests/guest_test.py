import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.songs = [
            Song("Africa", "Toto"),
            Song("Don't Stop Believin'", "Journey"),
            Song("Wonderwall", "Oasis"),
            Song("Uptown Girl", "Billy Joel"),
            Song("Ring of Fire", "Johnny Cash")
        ]
    
    def test_can_make_a_guest_with_name(self):
        guest = Guest("Rick", 0)
        expected = "Rick"
        actual = guest.name
        self.assertEqual(expected, actual)

    def test_guest_has_a_wallet(self):
        guest = Guest("Rick", 0)
        expected = 0
        actual = guest.wallet
        self.assertEqual(expected, actual)

    def test_can_pass_in_value_to_wallet(self):
        guest = Guest("Ricky", 20)
        expected = 20
        actual = guest.wallet
        self.assertEqual(expected, actual)

    def test_guest_knows_if_theyre_in_a_room(self):
        guest = Guest("Ricky", 20)
        expected = False
        actual = guest.in_room
        self.assertEqual(expected, actual)

    def test_guest_in_room_knows_theyve_entered(self):
        guest = Guest("Ricky", 20)
        guest.changed_location()
        expected = True
        actual = guest.in_room
        self.assertEqual(expected, actual)

    def test_guest_knows_theyve_left_room(self):
        guest = Guest("Ricky", 20)
        guest.changed_location()
        guest.changed_location()
        expected = False
        actual = guest.in_room
        self.assertEqual(expected, actual)

    def test_entering_a_room_decreases_wallet_amount(self):
        guest = Guest("Ricky", 20)
        guest.spend_money(15)
        expected = 5
        actual = guest.wallet
        self.assertEqual(expected, actual)

    def test_guest_might_have_favourite_song(self):
        guest = Guest("Morty", 20)
        actual = guest.favourite_song
        self.assertIsNone(actual)

    def test_guest_has_a_favourite_song(self):
        guest = Guest("Morty", 20, "Macarana")
        expected = "Macarana"
        actual = guest.favourite_song
        self.assertEqual(expected, actual)

    def test_guest_excited_if_favourite_song_in_room(self):
        guest = Guest("Jimmy", 60, "Africa")
        expected = "Wooooo!"
        actual = guest.thats_my_jam(self.songs)
        self.assertEqual(expected, actual)

    # def test_guest_favourite_song_not_in_playlist
        