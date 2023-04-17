class Merchant:
    def __init__(self, name, activated = True, id=None):
        self.name = name
        self.activated = activated
        self.id = id

    def mark_deactivated(self):
        self.activated = False
