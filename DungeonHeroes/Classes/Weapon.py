class InitialiseWeapon(object):
    def __init__(self, name, damage, weaponType, desc, weight):  # Constructor
        self.name = name
        self.damage = damage
        self.weaponType = weaponType  # Axe, Bow, Sword, etc.
        self.desc = desc  # Description of weapon
        self.weight = weight  # How much it weighs

    # Here we create a method to print information.
    # Example: rustySword.info()
    def info(self):
        print('Name: ' + self.name)
        print('Damage: ' + str(self.damage))
        print('Type: ' + self.weaponType)
        print('Weight: ' + str(self.weight))
        print('Description: ' + self.desc)

    def infoShort(self):
        print(self.name)
