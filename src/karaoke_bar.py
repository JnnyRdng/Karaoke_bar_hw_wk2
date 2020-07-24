from src.room import Room
from src.guest import Guest
from src.song import Song


class KaraokeBar:
    def __init__(self, name):
        self.name = name
        self.guests = [
            Guest("Frodo"),
            Guest("Sam"),
            Guest("Pippin"),
            Guest("Merry"),
            Guest("Bilbo"),
            Guest("Gandalf"),
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

    def make_playlist(self, songs):
        return [1, 2, 3, 4, 5]

