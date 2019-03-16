class InitialiseQuest(object):
    def __init__(self, name, desc, stage, questAmount, rewardtype, reward, finished):  # Constructor
        self.name = name
        self.desc = desc
        self.stage = stage  # Stage the quest is at complete/during/beginning
        self.questAmount = questAmount  # Amount of items required to fulfil quest
        self.rewardtype = rewardtype  # Type of reward
        self.reward = reward  # Reward for Q
        self.finished = finished  # If Done

    def info(self):
        print('Name: ' + self.name)
        print('Description: ' + self.desc)
        print()

    def infoShort(self):
        print(self.name)
