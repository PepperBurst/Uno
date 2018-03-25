import random
from Card import *

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in ['Red', 'Yellow', 'Green', 'Blue']:
            for v in range(0, 10):
                if(v != 0):
                    self.cards.append(Card(c, str(v)))
                self.cards.append(Card(c, str(v)))

    def show(self):
        for card in self.cards:
            card.show()
        # print("Card Length = " + str(len(self.cards)))

    def shuffle(self):
        for i in range(len(self.cards)-1, -1, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def isEmpty(self):
        empty = False
        if not self.cards:
            empty = True
        return empty

    def returnToDeck(self, pile, shuffleCount):
        self.cards = pile.cards.copy()
        pile.removeAll()
        for i in range(shuffleCount):
            self.shuffle()
