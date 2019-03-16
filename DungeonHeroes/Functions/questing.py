import time


def start(npc, player):
    count = 0
    exists = any(q for q in player.inventory if q.name.lower() == npc.quest.name.lower())
    if exists:
        for item in player.inventory:
            if item.name.lower() == npc.quest.name.lower():
                count += 1
                player.inventory.remove(item)
        if count == npc.quest.questAmount:
            npc.quest.stage = "complete"
            print(npc.name + ' has taken ' + npc.quest.name.lower() + ' from you.')
    elif npc.quest.rewardtype == 'gold':
        if player.gold >= npc.quest.questAmount:
            npc.quest.stage = "complete"
            player.gold -= npc.quest.questAmount
            print(npc.name + ' has taken ' + str(npc.quest.questAmount) + ' gold from you.')

    if npc.quest.stage == "complete":
        print('Thank you so much! My Hero!')
        time.sleep(2)
        if npc.quest.finished == True:
            print('Dont be greedy, you already got your reward! >:(')
        if npc.quest.finished == False:
            print('Here is your reward! Thanks again!')
            if npc.quest.rewardtype == "item":
                player.inventory.append(npc.quest.reward)
                print()
                print('You received the ' + npc.quest.reward.name)
                print()
            else:
                print()
                print('You have received ' + str(npc.quest.reward) + ' gold!')
                print()
                player.gold += npc.quest.reward

            npc.quest.finished = True

    if npc.quest.stage == "during":
        print('Hurry up and finish that quest!')

    if npc.quest.stage == "begin":
        print(player.name + ', i must give you this tough quest. Please do me this favour!')
        print(npc.name + ' hands you a small note:')
        time.sleep(4)
        npc.quest.info()
        npc.quest.stage = "during"
