import random
from Classes import Weapon, Skill, Shield


class InitialiseCharacter(object):
    def __init__(self, name, hp, mp, weight, gold, exp, desc, equipped):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weight = weight  # Amount the character can carry.
        self.skills = []  # Empty list of Skills for character.
        self.inventory = []  # Empty Inventory space for items.
        self.gold = gold  # Amount of current gold coins.
        self.exp = exp  # Experience gained.
        self.desc = desc  # Description of character.
        self.equipped = {
            "weaponEquipped": None,
            "shieldEquipped": None
        }  # Gear equipped dictionary

    # Here we create a method to print information.
    # Example: warrior.info()
    def info(self):
        print('****************************************************')
        print('********~~~~Your Character Stats~~~~*****************')
        print('****************************************************')
        print('HP: ' + str(self.hp))
        print('MP: ' + str(self.mp))
        print('Max Weight: ' + str(self.weight))
        print('Skills: [')
        for skill in self.skills:
            skill.infoShort()
        print(']')
        print('Inventory: [')
        for item in self.inventory:
            item.infoShort()
        print(']')
        print('Current Exp: ' + str(self.exp))
        print('Current Gold: ' + str(self.gold))
        print('Description: ' + self.desc)
        print('****************************************************')
        print()

    def charIntro(self, charChoice):
        if charChoice == '1':
            print('"JUST WHAT THIS OLD KNIGHT WAS LOOKING FOR!" ಠ_ృ')
        elif charChoice == '2':
            print('"MAYBE MY MAGIC CAN DISPELL THIS SORCERY!" (∩｀-´)⊃━☆ﾟ.*･｡ﾟ')
        elif charChoice == '3':
            print('"THEYLL NEVER SEE ME COMING!" ヽ( ﾟｰﾟ)ﾉ}　　　–→')
        elif charChoice == '4':
            print('"*GRUNT*" ( う-´)づ')
        print()

    def charTown(self, charChoice):
        if charChoice == '1':
            print('ಠ_ృ "Hmmmm, this place is rather strange..."')
        elif charChoice == '2':
            print('(∩｀-´)⊃━☆ "Maybe I can hone my magical abilities here.."')
        elif charChoice == '3':
            print('ヽ( ﾟｰﾟ)ﾉ} "I wonder can they see me..."')
        elif charChoice == '4':
            print('( う-´) "*GROWLS*"')
        print()

    def charQuestStart(self, charChoice):
        if charChoice == '1':
            print('ಠ_ృ "A worthy task, for an old honourable knight!"')
        elif charChoice == '2':
            print('(∩｀-´)⊃━☆ "Time to put my magic where my mouth is..."')
        elif charChoice == '3':
            print('ヽ( ﾟｰﾟ)ﾉ} "Like a shadow in the night, this will be effortless..."')
        elif charChoice == '4':
            print('( う-´) "*SNARL!*"')
        print()

    def charQuestEnd(self, charChoice):
        if charChoice == '1':
            print('ಠ_ృ "It was my honour..."')
        elif charChoice == '2':
            print('(∩｀-´)⊃━☆ "Nothin beats my magic!"')
        elif charChoice == '3':
            print('ヽ( ﾟｰﾟ)ﾉ} "Easy peasy lemon squeezy.."')
        elif charChoice == '4':
            print('( う~´) "*AWWHOOOOOOOOOOO*"')
        print()

    def addSkill(self, newSkill):
        self.skills.append(newSkill)

    def unlockSkill(self, newUnlockedSkill):
        newUnlockedSkill.unlocked = True
        print('New Skill Gained! You can now use ' + newUnlockedSkill.name + '!')

    def addItem(self, newItem):
        self.inventory.append(newItem)
        print('Added ' + newItem.name + ' to your inventory.')

    def addExp(self, newExp):
        self.exp += newExp
        print('You gained ' + str(newExp) + ' EXP! Total exp now ' + str(self.exp) + '.')

    def addGold(self, newGold):
        self.gold += newGold
        print('You gained ' + str(newGold) + ' GOLD! Total gold now ' + str(self.gold) + '.')

    def combatMoves(self):
        print('''\nIt's your turn:\n1 - Attack\n2 - Use a Skill\n3 - Use an Item''')
        combatChoice = input('Choose your move: ')

        # Character Turns - attack, use skill, use item

        if combatChoice == '1':
            if (self.equipped.get('weaponEquipped') != None):
                return random.randint(self.equipped['weaponEquipped'].damage - 1,
                                      self.equipped['weaponEquipped'].damage + 1)
            else:
                accident = random.randint(-1, 1)
                if (accident < 0):
                    print('\nOh no! You accidently healed the enemy! :/')
                return accident
        if combatChoice == '2':
            print('use skill')
        if combatChoice == '3':
            print('use item')

    def equipGear(self, item, itemType):
        self.equipped[itemType + "Equipped"] = next((i for i in self.inventory if i.name == item.name), None)
        print('You have equipped ' + self.equipped[itemType + "Equipped"].name)


def create(characterChoice):
    if characterChoice == '1':

        # Creating the Templar
        templar = InitialiseCharacter(
            name='Templar',
            hp=100,
            mp=50,
            weight=100,
            gold=0,
            exp=0,
            desc='''An old experienced Knight left over from the Crusades. His grey and white hair, scars, and steely gaze are all that remain. He wears an eye patch to cover the hole were his eye used to be, along with rusted armor, a shield that embraces the red and white colours of the Knights Templar...''',
            equipped={}
        )

        # Creating Skills
        bash = Skill.InitialiseSkill(
            'Bash', 6, 5, 0, 'Bash enemy with shield.', False)
        divineTouch = Skill.InitialiseSkill(
            'Divine Touch', 0, 20, 40, 'Heals the Templar to full HP. Can only be used once!', False)
        cluckVoience = Skill.InitialiseSkill(
            'Cluck Voience', 0, 50, 100, 'Turns an enemy into a loveable chicken. Only works on normal enemies.', False)

        # Add Skills to Character
        templar.addSkill(bash)
        templar.addSkill(divineTouch)
        templar.addSkill(cluckVoience)

        # Creating Starting Gear
        rustySword = Weapon.InitialiseWeapon(
            'Rusty Sword',
            20,  # TODO CHANGE
            'Short Sword',
            'An old rusted sword. This sword must be hundreds of years old.',
            10)
        woodenShield = Shield.InitialiseShield(
            'Old Wooden Shield', 10,
            'Kite Shield',
            'An old wooden shield in the shape of a kite. Used mostly by Knights.',
            20)

        # Adding starting gear to Inventory
        templar.addItem(rustySword)
        templar.addItem(woodenShield)

        # Equipping starting gear
        templar.equipGear(rustySword, "weapon")
        templar.equipGear(woodenShield, "shield")

        return templar

    elif characterChoice == '2':
        # do create
        wizard = InitialiseCharacter(
            name='Wizard',
            hp=50,
            mp=100,
            weight=70,
            gold=0,
            exp=0,
            desc='''He is an old man with limitless amount of magic power from a difrent land. He was the most powerfull out of his kind and now he stands here ready for what what will come to him...''',
            equipped={}
        )

        # Creating Skills
        # name, damage, mpReq, expReq, desc
        fireball = Skill.InitialiseSkill(
            'Fireball', 6, 10, 0, 'Shoots a ball of fire at the enemy.', False)
        splitIllusion = Skill.InitialiseSkill(
            'Split Ilusion', 0, 20, 40, 'The wizard creates a decoy of himself to shield attacks.', False)
        soulsavior = Skill.InitialiseSkill(
            'Soulsavior', 0, 50, 100, 'Kills enemy and heals wizard up to full health.', False)

        # Add Skills to Character
        wizard.addSkill(fireball)
        wizard.addSkill(splitIllusion)
        wizard.addSkill(soulsavior)

        # Creating Starting Gear
        # name, damage, weaponType, desc, weight
        longstick = Weapon.InitialiseWeapon(
            'longstick',
            1,
            'staff',
            'A simple stick off a tree.',
            10)
        bookShield = Shield.InitialiseShield(
            'Book of Skellia', 20,
            'Book Shield',
            'An old book. The pages are made from crystal. The words spoken protect the user.',
            5)

        # Adding starting gear to Inventory
        wizard.addItem(longstick)
        wizard.addItem(bookShield)

        # Equipping starting gear
        wizard.equipGear(longstick, "weapon")
        wizard.equipGear(bookShield, "shield")

        return wizard

    elif characterChoice == '3':
        archer = InitialiseCharacter(
            name='Archer',
            hp=70,
            mp=70,
            weight=60,
            gold=0,
            exp=0,
            desc='''A brave young Archer left over from the battles. He travels mystically around. With him near you, you really would want to turn around and run. Every battle makes him stronger, smarter and last but not least, it makes him want more...''',
            equipped={}
        )
        # Creating Skills
        # name, damage, mpReq, expReq, desc
        freezeArrow = Skill.InitialiseSkill(
            'Freeze Arrow', 0, 10, 0, 'Freeze the enemy with a Frozen Arrow!', False)
        powerDraw = Skill.InitialiseSkill(
            'Power Draw', 1, 5, 40, 'Charge up and fire a thunderous arrow!', False)
        shadowCloak = Skill.InitialiseSkill(
            'Shadow Cloak', 0, 40, 100, 'Vanish to be unseen for 2 turns!', False)

        # Add Skills to Character
        archer.addSkill(freezeArrow)
        archer.addSkill(powerDraw)
        archer.addSkill(shadowCloak)

        # Creating Starting Gear
        oldBow = Weapon.InitialiseWeapon(
            'Old Bow',
            2,
            'Bow',
            'An old rusted bow. This bow must be hundreds or thousands of years old.', 10)
        rustedDagger = Weapon.InitialiseWeapon(
            'Rusted Dagger',
            5,
            'Dagger',
            'An old rusted dagger. People say not one were killed with this rusted weapon.',
            20)
        # Adding starting gear to Inventory
        archer.addItem(oldBow)
        archer.addItem(rustedDagger)

        # Equipping starting gear
        archer.equipGear(oldBow, "weapon")

        return archer

    elif characterChoice == '4':
        warrior = InitialiseCharacter(
            name='Warrior',
            hp=120,
            mp=50,
            weight=120,
            gold=0,
            exp=0,
            desc='''A brave young warrior out to fight the whole world. He was sent from the king to do all types of quests. He is a very good damage dealer but is a bit out of shape, through the story he might become fitter, you might even call him OP!''',
            equipped={}
        )
        # name, damage, mpReq, expReq, desc
        shieldSaviour = Skill.InitialiseSkill(
            'Shield Saviour', 0, 15, 0, 'The warrior raises his arms to create a shield infront of him.', False)
        chargeAttack = Skill.InitialiseSkill(
            'Charge Attack', 5, 10, 40, 'The warrior charges at his enemy doing extra damage.', False)
        warCry = Skill.InitialiseSkill(
            'War Cry', 0, 40, 100, 'The warrior bellows his voice causing enemies to turn against each other.', False)

        # Add Skills to Character
        warrior.addSkill(shieldSaviour)
        warrior.addSkill(chargeAttack)
        warrior.addSkill(warCry)

        rustyAxe = Weapon.InitialiseWeapon(
            'Rusty Axe',
            1,
            'Axe',
            'An old rusty axe .',
            10)
        copperShield = Shield.InitialiseShield(
            'Copper Shield', 10,
            'Coppe',
            'An old metally shield.',
            20)

        # Adding starting gear to Inventory
        warrior.addItem(rustyAxe)
        warrior.addItem(copperShield)

        # Equipping starting gear
        warrior.equipGear(rustyAxe, "weapon")
        warrior.equipGear(copperShield, "shield")

        return warrior
