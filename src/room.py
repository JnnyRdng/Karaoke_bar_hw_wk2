class Room:
    def __init__(self):
        self.guests = []
        self.playlist = []
        self.max_size = 3

    def start_playlist(self, playlist):
        self.playlist += playlist

    def add_guest_to_room(self, guest):
        if self.room_has_space():
            self.guests.append(guest)
            return True
        return False

    def remove_guest(self, guest):
        in_room = self.is_guest_in_room(guest)
        if in_room:
            self.guests.remove(guest)
        return in_room

    def is_guest_in_room(self, guest):
        return guest in self.guests

    def return_guest_list(self):
        return self.guests

    def room_has_space(self):
        if len(self.guests) >= self.max_size:
            return False
        return True