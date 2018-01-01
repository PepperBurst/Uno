class Card(object):
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

    def show(self):
        print(self.colour + " " + self.value)

    def get(self):
        return str(self.colour + " " + self.value)
