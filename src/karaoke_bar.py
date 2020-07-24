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
            Guest("Gandalf")
        ]
