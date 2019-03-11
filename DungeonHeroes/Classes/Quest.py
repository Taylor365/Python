class InitialiseQuest(object):
    def __init__(self, name, desc, trigger, stage, reward, finished):  # Constructor
        self.name = name
        self.desc = desc
        self.trigger = trigger  # This is what starts the Q
        self.stage = stage  # Stage the quest is at complete/during/beginning
        self.reward = reward  # Reward for Q
        self.finished = finished  # If Done

    def info(self):
        print('Name: ' + self.name)
        print('Description: ' + self.desc)
        print('Stage: ' + self.stage)
        print('Reward: ' + self.reward)
        print()

    def infoShort(self):
        print(self.name)
