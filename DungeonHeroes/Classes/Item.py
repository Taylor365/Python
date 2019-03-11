class InitialiseItem(object):
    def __init__(self, name, desc, effect, quest, cost):
        self.name = name
        self.desc = desc  # Description of item
        self.effect = effect  # Effect of item
        self.quest = quest  # If it is quest or not
        self.cost = cost  # Cost of item

    # Here we create a method to print information.
    # Example: woodenShield.info()
    def info(self):
        print('Name: ' + self.name)
        print('Effect : ' + str(self.effect))
        print('Cost: ' + str(self.cost))
        print('Description: ' + self.desc)

    def infoShort(self):
        print(self.name)
