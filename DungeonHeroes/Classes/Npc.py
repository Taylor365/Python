class InitialiseNpc(object):
    # Create NPC
    def __init__(self, name, quest, shopKeep, desc):  # Constructor
        self.name = name
        self.quest = quest  # Check if they have a quest
        self.shopKeep = shopKeep  # Check if they are shopkeeper
        self.desc = desc  # Description of the Npc

    def info(self):
        print('Name: ' + self.name)
        print('Description: ' + self.desc)
        print()

    def infoShort(self):
        print(self.name)
