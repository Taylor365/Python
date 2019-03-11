class InitialiseShield(object):
    def __init__(self, name, blockChance, shieldType, desc, weight):
        self.name = name
        self.blockChance = blockChance  # Chance to block attack
        self.shieldType = shieldType  # Round, Kite, Tower, etc.
        self.desc = desc  # Description of shield
        self.weight = weight  # How much it weighs

    # Here we create a method to print information.
    # Example: woodenShield.info()
    def info(self):
        print('Name: ' + self.name)
        print('Block Chance: ' + str(self.blockChance))
        print('Type: ' + self.shieldType)
        print('Weight: ' + str(self.weight))
        print('Description: ' + self.desc)

    def infoShort(self):
        print(self.name)
