from Functions import shopping
from Functions import questing


def interaction(Npc, Town, player):
    finished = False
    while finished == False:
        if Npc.shopKeep == True:
            shopChoice = input('1 - Talk\n2 - Shop\n3 - Exit\n\nSelect Your Choice: ')
            if shopChoice == '2':
                shopping.start(player, Town.shop)
            elif shopChoice == '3':
                finished = True
        if Npc.shopKeep == False:
            if Npc.hasquest == True:
                questChoice = input('1 - Talk\n2 - Quest\n3 - Exit\n\nSelect Your Choice: ')
                if questChoice == '2':
                    questing.start(Npc, player)
                elif questChoice == '3':
                    finished = True
            elif Npc.hasquest == False:
                talkChoice = input('1 - Talk\n2 - Exit\n\nSelect Your Choice: ')
                if talkChoice == '2':
                    finished = True
