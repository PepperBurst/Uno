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
            playerList.getPlayerAt(i).startDraw(deck)
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
        os.system('clear')

    def discardLoop(self, deck, pile, currentPlayer):
        # if(not currentPlayer.drawStatus()):
        discard = False
        skipTurn = False
        currentPlayer.displayHand()
        while((discard is False) and (skipTurn is False)):
            if(not currentPlayer.drawStatus):
                dropIndex = self.checkIndexRange(currentPlayer)
                if(self.checkDrop(dropIndex-1, pile, currentPlayer)):
                    #print(currentPlayer.getCardAt(dropIndex-1))
                    pile.discard(currentPlayer.discard(dropIndex-1))
                    discard = True
                else:
                    self.clear()
                    print('Choose another card to discard')
                    pile.showLast()
                    currentPlayer.displayHand()
            else:
                if(self.checkDiscard(deck, pile, currentPlayer)):
                    dropIndex = self.checkIndexRange(currentPlayer)
                    if(self.checkDrop(dropIndex-1, pile, currentPlayer)):
                        #print(currentPlayer.getCardAt(dropIndex-1))
                        pile.discard(currentPlayer.discard(dropIndex-1))
                        discard = True
                    else:
                        self.clear()
                        print('Choose another card to discard')
                        pile.showLast()
                        currentPlayer.displayHand()
                else:
                    print('The card you drew cannot be discarded. Skipping turn')
                    skipTurn = True
        currentPlayer.updateDrawStatus(False)

    def checkIndexRange(self, player):
        endLoop = False
        dropIndex = 0
        while endLoop is False:
            dropIndex = int(input('Choose card to discard: '))
            if(dropIndex > len(player.hand)):
                print('Index out of range!')
                print('Choose a number within the index range 1 to ' + str(len(player.hand)))
            else:
                endLoop = True
        return dropIndex

    def getTurnIncrement(self, playerList):
        turnIncrement = 0
        for player in playerList.list:
            if(player.done):
                turnIncrement =+ 1
        return turnIncrement

    # def isNextDone(self, player):
