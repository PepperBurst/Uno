class PlayerList(object):
    def __init__(self):
        self.list = []

    def addPlayer(self, player):
        self.list.append(player)

    def getPlayer(self, index):
        return self.list[index]

    def showAll(self):
        for i in range(len(self.list)):
            print('Player ' + str(i + 1) + ": " + self.list[i].getName())
