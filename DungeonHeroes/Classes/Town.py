from Classes import Enemy, Quest, Dungeon, Weapon, Shop, Npc


class InitialiseTown(object):
    def __init__(self, name, dungeon, shop, npcs, quests, desc):
        self.name = name  # Name of town
        self.dungeon = dungeon  # The town dungeon
        self.shop = shop  # The town shop
        self.npcs = []  # Empty list of NPCs in town.
        self.quests = []  # Empty list of Quests in town.
        self.desc = desc  # Description of the town.

    # Here we create a method to print information.
    # Example: town.info()
    def info(self):
        print('****************************************************')
        print('********~~~~Welcome to ' + self.name + '~~~~*****************')
        print('****************************************************')
        print(self.desc)

    def addNpc(self, newNPC):
        self.npcs.append(newNPC)

    def addQuest(self, newQuest):
        self.quests.append(newQuest)

    def addShop(self, newShop):
        self.shop = newShop

    def addDungeon(self, newDungeon):
        self.dungeon = newDungeon


def createTown(townChoice):
    enemies = Enemy.createEnemies(townChoice)

    if townChoice == 1:

        # Creating the Town
        # name, dungeon, shop, npcs, quests, desc
        cardium = InitialiseTown(
            name='Cardium',
            dungeon=None,
            shop=None,
            npcs=[],
            quests=[],
            desc='''A once thriving town, now scarce and barren. 
            In the center stand a huge Monastery with a spiked tower that holds a clock and bell. 
            The clock doesn't seem to work and dark clouds surround the big structure. 
            There is also a few houses along the road with a shop.'''
        )

        # Creating Dungeon
        # name, dungeonEnemies, secretItem, desc, cleared
        monastery = Dungeon.InitialiseDungeon('The Monastery',
                            # name, damage, weaponType, desc, weight
                            Weapon.InitialiseWeapon('Secret', 5, 'Axe', 'Tis secret', 50),
                            '''An old stone monastery. It gives a spooky vibe...''',
                            False
                            )

        # Add Enemies to Dungeon
        monastery.addEnemies(enemies)

        # Add Dungeon to Town
        cardium.addDungeon(monastery)

        # Creating Quests
        # name, desc, stage, questAmount, rewardtype, reward, finished
        quest1 = Quest.InitialiseQuest('Bones',
                       '''Asha requires bones for her potion. Collect 3 bones from skeletons in the Monestary.''',
                       'begin', 3, 'gold', 25, False)
        grimSlayer = Weapon.InitialiseWeapon(
            'Grim Slayer',
            9,
            'sword',
            'The Legendary sword of Slaying.',
            10)
        quest2 = Quest.InitialiseQuest('Greed',
                       '''Grizzly's greed knows no bounds. He has found an extra special weapon you could use, but requires the coin! Collect 50 gold and Grizzly will hand it over...''',
                       'begin', 50, 'item', grimSlayer, False)
        quest3 = Quest.InitialiseQuest('From The Ashes',
                       '''Clear out the Monastery of skellingtons and bring life back to the town!''',
                       'begin', 100, 'gold', 75, False)

        # Creating NPCs
        # name, quest, shopKeep, desc
        asha = Npc.InitialiseNpc(
            'Asha', True, quest1, False, 'An old sorceress. She has lived in Cardium her entire life.')
        grizzly = Npc.InitialiseNpc(
            'Grizzly', True, quest2, True, 'A greedy shopkeeper. Only interested if you have coin.')
        kretian = Npc.InitialiseNpc(
            'Kretian', True, quest3, False, 'An old mercenary. He is blind but nothing escapes him.')

        # Add Npcs to Town
        cardium.addNpc(asha)
        cardium.addNpc(grizzly)
        cardium.addNpc(kretian)

        # name, desc, inventory, gold, shopkeeper
        grizzlyShop = Shop.InitialiseShop('Greedy Grizzlies',
                           'A dirty run-down shack. Not much here but old gear.',
                           [],
                           100,
                           grizzly)

        # Add Shop to Town
        cardium.addShop(grizzlyShop)

        # Adding quests to Town
        cardium.addQuest(quest1)
        cardium.addQuest(quest2)
        cardium.addQuest(quest3)

        return cardium

    elif townChoice == 2:
        duskValley = InitialiseTown(
            name='Dusk Valley',
            # name, enemyTypes, enemyAmount, quest, secretItem, desc, cleared
            dungeon=None,
            shop=None,
            npcs=[],
            quests=[],
            desc='''Welcome to Dusk Valley. 
            This a quiet town and everywhere is dark but people are opposite to the description of the town. 
            They're full of happiness and see the village as their home.'''
        )

        # Creating Dungeon
        # name, enemies, secretItem, desc, cleared
        mineshaft = Dungeon.InitialiseDungeon('The Mineshaft',
                            # name, damage, weaponType, desc, weight
                            Weapon.InitialiseWeapon('Secret', 5, 'Axe', 'Tis secret', 50),
                            '''An old stone mineshaft. It gives a minecraft vibe...''',
                            False
                            )

        # Add Dungeon to Town
        duskValley.addDungeon(mineshaft)

        # Creating Quests
        # name, desc, stage, rewardtype, reward, finished
        quest1 = Quest.InitialiseQuest('Collect 10 coins',
                       '''Collect 10 coins for a reward.''',
                       'begin', 10, 'item', 'INSERT COOL SHIELD', False)
        quest2 = Quest.InitialiseQuest('Saviour',
                       '''Shellies dad is inslaved by the demon king, slay the demon king to save her dad...''',
                       'begin', 100, 'item', 'INSERT LEGENDARY WEAPON', False)
        quest3 = Quest.InitialiseQuest('Slime',
                       '''Collect 2 slimes for a reward.''',
                       'begin', 2, 'gold', 25, False)

        # Creating NPCs
        # name, quest, shopKeep, desc
        geoff = Npc.InitialiseNpc(
            'Geoff', True, quest1, True, "A smelly villager. He doesn't like baths")
        shelly = Npc.InitialiseNpc(
            'Shelly', True, quest2, False, 'A beautiful princess.')
        nial = Npc.InitialiseNpc(
            'Nial', True, quest3, False, 'Nial the legendary miner.')

        # Add Npcs to Town
        duskValley.addNpc(shelly)
        duskValley.addNpc(geoff)
        duskValley.addNpc(nial)

        # name, desc, inventory, gold, shopkeeper
        geoffsGoodies = Shop.InitialiseShop('Geoffs Goodies',
                             'Wall to wall packed full of great gear!.',
                             [],
                             100,
                             geoff)

        # Add Shop to Town
        duskValley.addShop(geoffsGoodies)

        # Adding quests to Town
        duskValley.addQuest(quest1)
        duskValley.addQuest(quest2)
        duskValley.addQuest(quest3)

        return duskValley

    elif townChoice == 3:
        avondale = InitialiseTown(
            name='Avondale',
            # name, enemyTypes, enemyAmount, quest, secretItem, desc, cleared
            dungeon=None,
            shop=None,
            npcs=[],
            quests=[],
            desc='''A majestic town, now broken down from the wars. 
            In the center of the town stands a giant Monastery with a twisting and turning tower that holds a clock and bell. 
            The clock has rusted with the rats and pests sneaking about. 
            There is a few houses along the road in the town with a shop with a motto 'Contented with little, yet wishing for more'.'''
        )

        # Creating Dungeon
        # name, enemies, secretItem, desc, cleared
        mistyIsle = Dungeon.InitialiseDungeon('The Isle of Mist',
                            # name, damage, weaponType, desc, weight
                            Weapon.InitialiseWeapon('Secret', 5, 'Axe', 'Tis secret', 50),
                            '''An old stone misty Isle. It gives a misty vibe...''',
                            False
                            )

        # Add Enemies to Dungeon
        mistyIsle.addEnemies(enemies)

        # Add Dungeon to Town
        avondale.addDungeon(mistyIsle)

        # Creating Quests
        # name, desc, trigger, reqToFinish, reward, finished
        quest1 = Quest.InitialiseQuest('PhantomSkulls',
                       '''Thierican needs Phantom Skulls for his potion. Collect 2 Phantom Skulls from Phantoms from the Isle of Mist.''',
                       'begin', 2, 'gold', 20, False)

        boneSnapper = Weapon.InitialiseWeapon(
            'Bone Snapper',
            9,
            'bow',
            'The Legendary bow that requires supreme strength to draw.',
            10)
        quest2 = Quest.InitialiseQuest('Sphinx Hearts',
                       '''Lariyan needs Sphinx Hearts to have DNA tests on. 
                       Collect 1 Sphinx Hearts for him. You will have to kill Sphinxs. Remember, it will be harder than you think...''',
                       'begin', 1, 'item', boneSnapper, False)
        quest3 = Quest.InitialiseQuest('Goblin Trouble',
                       '''Zeaph is having a bit of a hard time with Goblins. He needs your help! Help him by killing the GOBLIN KING''',
                       'begin', 100, 'item', 'INSERT LEGENDARY WEAPON', False)

        # Creating NPCs
        # name, hasquest, quest, shopKeep, desc
        thierican = Npc.InitialiseNpc(
            'Thierican', True, quest1, True,
            'An old wizard. He is very powerful and smart... His spells can destory anything!')
        lariyan = Npc.InitialiseNpc(
            'Lariyan', True, quest2, False,
            "A young scientist. He is very cheeky and you won't see him outside his broken down lab.")
        zeaph = Npc.InitialiseNpc(
            'Zeaph', True, quest3, False,
            'He is a wonderer. He has no job and always gets himself tied up... But if given a chance, he will leave you dead!')

        # Add Npcs to Town
        avondale.addNpc(lariyan)
        avondale.addNpc(thierican)
        avondale.addNpc(zeaph)

        # name, desc, inventory, gold, shopkeeper
        thiericansShop = Shop.InitialiseShop("Thierican's Potion Hive",
                              "A dirty mess of potions (Thierican's own ones) that he calls a shop. If you need potions or wepons, this shop is for you.",
                              [],
                              100,
                              thierican)

        # Add Shop to Town
        avondale.addShop(thiericansShop)

        # Adding quests to Town
        avondale.addQuest(quest1)
        avondale.addQuest(quest2)
        avondale.addQuest(quest3)

        return avondale

    elif townChoice == 4:
        evillage = InitialiseTown(
            name='E-village',
            # name, enemyTypes, enemyAmount, quest, secretItem, desc, cleared
            dungeon=None,
            shop=None,
            npcs=[],
            quests=[],
            desc='''A once happy village, now sad and evil. 
            In the middle of this lonely village is a massive castle where the greedy king lives. 
            Some people even say it's haunted.'''
        )

        # Creating Dungeon
        # name, enemies, secretItem, desc, cleared
        castle = Dungeon.InitialiseDungeon('The Castle',
                         # name, damage, weaponType, desc, weight
                         Weapon.InitialiseWeapon('Secret', 5, 'Axe', 'Tis secret', 50),
                         '''An old stone monastery. It gives a spooky vibe...''',
                         False
                         )

        # Add Enemies to Dungeon
        castle.addEnemies(enemies)

        # Add Dungeon to Town
        evillage.addDungeon(castle)

        # Creating Quests
        # name, desc, trigger, reqToFinish, reward, finished
        quest1 = Quest.InitialiseQuest('Bananas',
                       '''Bob requires bananas for his banana bread . Collect 2 bananas from the farm at the edge of the village.''',
                       'begin', 2, 'gold', 25, False)
        quest2 = Quest.InitialiseQuest('Jolly',
                       'Jolly Joeys shop is haunted. Help him by terminating the monsters in ' + evillage.dungeon.name,
                       'begin', 100, 'gold', 55, False)
        deathSpike = Weapon.InitialiseWeapon(
            'Death Spike',
            9,
            'lance',
            'The Legendary lance of Death.',
            10)
        quest3 = Quest.InitialiseQuest('Dragon scale',
                       '''Help the gready king by killing the dragon and bringing back it's scale in return you'll recieve a Legendary item.!''',
                       'begin', 1, 'item', deathSpike, False)

        # Creating NPCs
        # name, quest, shopKeep, desc
        bob = Npc.InitialiseNpc(
            'Bob', True, quest1, False,
            'An old farmer. He has lived all his life in his farm and now is next in line to inherite the farm .')
        joe = Npc.InitialiseNpc(
            'Joey', True, quest2, True, 'A friendly shopkeeper. Always has what you need.')
        kingEval = Npc.InitialiseNpc(
            'Eval', True, quest3, False, 'A rich, greedy king. He owns the town so he thinks he owns everyone.')

        # Add Npcs to Town
        evillage.addNpc(bob)
        evillage.addNpc(joe)
        evillage.addNpc(kingEval)

        # name, desc, inventory, gold, shopkeeper
        jollyJoeys = Shop.InitialiseShop('Jolly Joeys',
                          'A fun and jolly shop. He sales all type of stuff from bones to apples.',
                          [],
                          100,
                          joe)

        # Add Shop to Town
        evillage.addShop(jollyJoeys)

        # Adding quests to Town
        evillage.addQuest(quest1)
        evillage.addQuest(quest2)
        evillage.addQuest(quest3)

        return evillage
