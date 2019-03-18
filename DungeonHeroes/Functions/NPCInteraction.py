from Functions import shopping
from Functions import questing


def interaction(npc, town, player):
    finished = False
    while not finished:
        if npc.shopKeep:
            shopChoice = input('1 - Talk\n2 - Shop\n3 - Quest\n4 - Exit\n\nSelect Your Choice: ')
            if shopChoice == '2':
                shopping.start(player, town.shop)
            elif shopChoice == '3':
                questing.start(npc, player, town)
            elif shopChoice == '4':
                finished = True
        else:
            if npc.hasquest:
                questChoice = input('1 - Talk\n2 - Quest\n3 - Exit\n\nSelect Your Choice: ')
                if questChoice == '2':
                    questing.start(npc, player, town)
                elif questChoice == '3':
                    finished = True
            elif not npc.hasquest:
                talkChoice = input('1 - Talk\n2 - Exit\n\nSelect Your Choice: ')
                if talkChoice == '2':
                    finished = True
