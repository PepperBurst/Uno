import random
import os

class Game(object):
    def __int__(self):
        self.currentHand = []
        self.lastDiscard
        self.dropCard

    def start(self, deck, pile, playerCount, playerList):
        print('Starting game...')
        print('Dealing cards...')
        print('Game start')
        firstTurn = random.randint(0, playerCount-1)
        for i in range(playerCount):
            playerList.getPlayer(i).startDraw(deck)
        pile.discard(deck.drawCard())
        return firstTurn

    def checkDiscard(self, deck, pile, player):
        dropCard = False
        self.lastDiscard = pile.getLast()
        self.currentHand = []
        for card in player.hand:
            self.currentHand.append(card)
        for i in range(len(self.currentHand)):
            if(self.currentHand[i].colour == self.lastDiscard.colour):
                dropCard = True
            elif(self.currentHand[i].value == self.lastDiscard.value):
                dropCard = True
        return dropCard

    def checkDrop(self, index, pile, player):
        dropCard = False
        self.lastDiscard = pile.getLast()
        self.dropCard = player.getCardAt(index) #-1
        if(self.lastDiscard.colour == self.dropCard.colour):
            dropCard = True
        elif(self.lastDiscard.value == self.dropCard.value):
            dropCard = True
        return dropCard

    def clear(self):
        os.system('cls')

    def discardLoop(self, deck, pile, currentPlayer):
        discard = False
        currentPlayer.displayHand()
        while discard is False:
            dropIndex = int(input('Choose card to discard: '))
            if(self.checkDrop(dropIndex-1, pile, currentPlayer)):
                #print(currentPlayer.getCardAt(dropIndex-1))
                pile.discard(currentPlayer.discard(dropIndex-1))
                discard = True
            else:
                self.clear()
                print('Choose another card to discard')
                pile.showLast()
                currentPlayer.displayHand()
