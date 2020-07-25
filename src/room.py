class Room:
    def __init__(self):
        self.guests = []
        self.playlist = []

    def start_playlist(self, playlist):
        self.playlist += playlist

    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        in_room = self.is_guest_in_room(guest)
        if in_room:
            self.guests.remove(guest)
        return in_room

    def is_guest_in_room(self, guest):
        return guest in self.guests

    def return_guest_list(self):
        return self.guests