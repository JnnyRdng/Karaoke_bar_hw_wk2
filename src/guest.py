class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.in_room = False

    def changed_location(self):
        self.in_room = True