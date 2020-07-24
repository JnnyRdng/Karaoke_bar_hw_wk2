class Room:
    def __init__(self):
        self.guests = []
        self.playlist = []

    def start_playlist(self, playlist):
        self.playlist += playlist
    
    def add_guest_to_room(self, guest):
        self.guests.append(guest)