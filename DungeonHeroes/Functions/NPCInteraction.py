def interaction(Npc, Town, player):
    finished = False
    while finished == False:
        if Npc.shopKeep == True:
            shopChoice = input('1 - Talk\n2 - Shop\n3 - Exit')
            if shopChoice == '2':
                shopping(player, Town.shop)
            elif shopChoice == '3':
                finished = True
        if Npc.shopKeep == False:
            if Npc.quest == True:
                questChoice = input('1 - Talk\n2 - Quest\n3 - Exit')
                if questChoice == '2':
                    questing(Npc, player)
                elif questChoice == '3':
                    finished = True
            elif Npc.quest == False:
                talkChoice = input('1 - Talk\n2 - Exit')
                if talkChoice == '2':
                    finished = True