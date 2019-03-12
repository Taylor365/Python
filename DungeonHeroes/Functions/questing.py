import time


def start(npc, player):
    if npc.quest.stage == "complete":
        print('Thank you so much! My Hero!')
        if npc.quest.finished == True:
            print('Dont be greedy, you already got your reward! >:(')
            if npc.quest.finished == False:
                print('Here is your reward! Thank you so much Hero!')
                if npc.quest.rewardtype == "item":
                    player.inventory.append(npc.quest.reward)
                else:
                    player.gold += npc.quest.reward

                npc.quest.finished = True
    if npc.quest.stage == "during":
        print('Hurry up and finish that quest!')
    if npc.quest.stage == "begin":
        print(player.name + ', i must give you this tough quest. Please do me this favour!')
        print(npc.name + ' hands you a small note:')
        time.sleep(2)
        npc.quest.info()
        npc.quest.stage = "during"
