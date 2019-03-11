class InitialiseSkill(object):
    def __init__(self, name, damage, mpReq, expReq, desc, unlocked):  # Constructor
        self.name = name
        self.damage = damage
        self.mpReq = mpReq  # How much MP it requires to use
        self.expReq = expReq  # How much Exp is required to unlock
        self.desc = desc  # Description of the skill
        self.unlocked = unlocked  # If skill is locked

    def info(self):
        print('Name: ' + self.name)
        print('Damage : ' + str(self.damage))
        print('MP: ' + str(self.mpReq))
        print('Experience required to unlock: ' + str(self.expReq))
        print('Description: ' + self.desc)
        print()

    def infoShort(self):
        print(self.name)
