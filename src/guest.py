class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.in_room = False
        self.favourite_song = None

    def changed_location(self):
        self.in_room = not self.in_room

    def spend_money(self, amount):
        self.wallet -= amount