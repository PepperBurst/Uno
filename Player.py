class Player(object):
    playerCount = 0
    def __init__(self):
        self.hand = []
        Player.playerCount += 1

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def startDraw(self, deck):
        for c in range(7):
            self.hand.append(deck.drawCard())

    def showHand(self):
        handCount = 1
        for card in self.hand:
            print(str(handCount) + ": " + card.get())
            handCount += 1

    def discard(self, index):
        return self.hand.pop(index)

    def displayDraw(self):
        print('You drew ' + self.hand[-1].get())

    def isHandEmpty(self):
        empty = False
        if not self.hand:
            empty = True
        return empty

    def getCardAt(self, index):
        return self.hand[index]

    def displayHand(self):
        print(self.getName() + "\'s hand:")
        self.showHand()
