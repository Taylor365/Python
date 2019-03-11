class InitialiseShop(object):
    def __init__(self, name, desc, inventory, gold, shopkeeper):
        self.name = name
        self.desc = desc  # Description
        self.inventory = []  # Shop Items
        self.gold = gold  # Gold in shop
        self.shopkeeper = shopkeeper  # Shopkeeper

    def info(self):
        print('Name: ' + self.name)
        print('Description: ' + self.desc)
        print('Shopkeeper: ' + self.shopkeeper)
        print()

    def infoShort(self):
        print(self.name)
