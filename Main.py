from Card import *
from Deck import *
from Player import *
from PlayerList import *
from Game import *
from Pile import *
import random

print('Uno')

playerList = PlayerList()
deck = Deck()
pile = Pile()
gameEnd = False

playerCount = int(input('Enter number of Players: '))
players = [Player() for i in range(playerCount)]
for p in players:
    playerList.addPlayer(p)
for i in range(len(players)):
    name = input('Enter player ' + str(i + 1) + " name: ")
    playerList.getPlayer(i).setName(name)
shuffleCount = int(input('Shuffle the deck how many times?: '))
for s in range(shuffleCount):
    deck.shuffle()
print('Deck shuffled ' + str(shuffleCount) + " time(s)")
# while gameEnd is False:
game = Game()
turn = game.start(deck, pile, playerCount, playerList)
totalTurn = 0

while gameEnd is False:
    game.clear()
    pile.showLast()
    currentPlayer = playerList.getPlayer(turn)
    if(game.checkDiscard(deck, pile, currentPlayer)):
        game.discardLoop(deck, pile, currentPlayer)
    else:
        print('No eligible cards to discard')
        print('Drawing a card from the deck...')
        currentPlayer.draw(deck)
        currentPlayer.displayDraw()
        currentPlayer.displayHand()
        game.discardLoop(deck, pile, currentPlayer)

    turn += 1
    if(turn > playerCount-1):
        turn = 0
    totalTurn +=1
    if(currentPlayer.isHandEmpty()):
        print(currentPlayer.getName() + " wins!")
        gameEnd = True
    if(deck.isEmpty()):
        print('Draw: Ran out of deck cards')
        gameEnd = True

# gameEnd = True
# deck = Deck()
# deck.shuffle()
# List.getPlayer(0).draw(deck)
# List.getPlayer(0).showHand()
# List.getPlayer(1).draw(deck)
# List.getPlayer(1).showHand()
# List.showAll()
