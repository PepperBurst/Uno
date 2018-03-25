class Pile(object):
    def __init__(self):
        self.cards = []

    def discard(self, card):
        self.cards.append(card)

    def showAll(self):
        for card in self.cards:
            card.show()

    def showLast(self):
        card = self.cards[-1]
        print('Last Discard: ' + card.get())

    def getLast(self):
        return self.cards[-1]

    def removeAll(self):
        self.cards.clear()
        
