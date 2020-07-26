from random import randint

from src.room import Room
from src.guest import Guest
from src.song import Song


class KaraokeBar:
    def __init__(self, name):
        self.name = name
        self.guests = [
            Guest("Frodo", 50),
            Guest("Sam", 40),
            Guest("Pippin", 40),
            Guest("Merry", 50),
            Guest("Bilbo", 1),
            Guest("Gandalf", 50),
        ]
        self.songs = [
            Song("Africa", "Toto"),
            Song("Don't Stop Believin'", "Journey"),
            Song("Wonderwall", "Oasis"),
            Song("Uptown Girl", "Billy Joel"),
            Song("Ring of Fire", "Johnny Cash"),
            Song("Angels", "Robbie Williams"),
            Song("My Way", "Frank Sinatra"),
            Song("Wannabe", "Spice Girls"),
        ]
        self.rooms = [Room(), Room()]
        self.guests_in_rooms = []

    def find_guest_by_name(self, name):
        for guest in self.guests:
            if guest.name == name:
                return guest
        for guest in self.guests_in_rooms:
            if guest.name == name:
                return guest

    def make_playlist(self, songs):
        seen_index = []
        playlist = []
        while len(playlist) < 5:
            index = randint(0, len(self.songs) - 1)
            if index not in seen_index:
                playlist.append(self.songs[index])
            seen_index.append(index)
        return playlist

    def send_guest_to_room(self, guest):
        for room in self.rooms:
            if room.add_guest_to_room(guest) and room.enough_money(guest):
                self.guests_in_rooms.append(guest)
                guest.changed_location()
                self.guests.remove(guest)
                break
            
    def grant_admission(self, guest):
        self.guests.append(guest)

    def return_guest_from_room(self, guest):
        for room in self.rooms:
            guest_list = room.return_guest_list()
            if guest in guest_list:
                room.remove_guest(guest)
                self.guests_in_rooms.remove(guest)
                self.guests.append(guest)
                break
