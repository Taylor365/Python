def questing(npc, player):
    if npc.quest.queststage == "complete":
        print('complete')
        if npc.quest.finished == True:
            print('Dont be greedy')
            if npc.quest.finished == False:
                print('Reward given')
                player.inventory.append(npc.quest.reward)
                npc.quest.finished = True
    if npc.quest.queststage == "during":
        print('During')
    if npc.quest.queststage == "begin":
        print('begin')
