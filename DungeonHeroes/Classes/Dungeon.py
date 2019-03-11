class InitialiseDungeon(object):
    def __init__(self, name, secretItem, desc, cleared):  # Constructor
        self.name = name
        self.dungeonEnemies = []  # The enemies
        self.secretItem = secretItem  # The secret Item in the dungeon
        self.desc = desc  # Description of the Dungeon
        self.cleared = cleared  # Check if finished

    def info(self):
        print('Name: ' + self.name)
        print('Description: ' + self.desc)
        print()

    def infoShort(self):
        print(self.name)

    def addEnemies(self, newEnemies):
        self.dungeonEnemies = newEnemies
