class PlayerList(object):
    def __init__(self):
        self.list = []

    def addPlayer(self, player):
        self.list.append(player)

    def getPlayerAt(self, index):
        return self.list[index]

    def showAll(self):
        for i in range(len(self.list)):
            print('Player ' + str(i + 1) + ": " + self.list[i].getName())

    def getLastPlayer(self):
        doneStatus = []
        for p in self.list:
            doneStatus.append(p.isDone())
        lastPlayer = [i for i, x in enumerate(doneStatus) if not x]
        return self.list[lastPlayer[0]]
