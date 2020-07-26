import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
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
