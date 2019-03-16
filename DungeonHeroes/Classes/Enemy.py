import random
from Classes import Item


class InitialiseEnemy(object):
    def __init__(self, name, hp, damage, enemyType, desc, treasureClass, goldDrop, expDrop):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.enemyType = enemyType  # Type of enemy, normal, boss, etc.
        self.desc = desc  # Description of enemy
        self.treasureClass = treasureClass  # What level of item they can drop
        self.goldDrop = goldDrop  # Gold to drop
        self.itemDrop = []  # Items to drop
        self.expDrop = expDrop  # Experience to give

    def info(self):
        print('Name: ' + self.name)
        print('HP: ' + str(self.hp))
        print('Type: ' + self.enemyType)
        print('Description: ' + self.desc)

    # Enemy Turns - attack, use skill
    def combatMoves(self):
        damage = self.damage
        damage = random.randint((damage - 2), (damage + 2))
        return damage

    def addItemDrop(self, newItem):
        self.itemDrop.append(newItem)


def createEnemies(townChoice):
    enemies = []

    if townChoice == 1:
        # Create quest items that the enemies will hold
        # name, desc, effect, quest, cost
        bones = Item.InitialiseItem(
            name='Bones',
            desc='Bones collected from skellingtons',
            effect=0,
            quest=True,
            cost=0
        )

        skullKey = Item.InitialiseItem(
            name='Skull Key',
            desc='A key made from bone...',
            effect=0,
            quest=True,
            cost=0
        )

        # name, hp, enemyType, desc, treasureClass, goldDrop, itemDrop, expDrop
        skellington = InitialiseEnemy(
            name='Skellington',
            hp=10,
            damage=random.randint(2, 5),
            enemyType='normal',
            desc='''Scary spooky skeleton''',
            treasureClass=1,
            goldDrop=random.randint(0, 5),
            expDrop=2
        )

        skellington.addItemDrop(bones)

        skellingtonHound = InitialiseEnemy(
            name='Skellington Hound',
            hp=5,
            damage=random.randint(2, 3),
            enemyType='normal',
            desc='''Scary spooky skeleton doggy made of bones''',
            treasureClass=1,
            goldDrop=random.randint(0, 2),
            expDrop=1
        )

        skellingtonHound.addItemDrop(bones)

        skellingtonKing = InitialiseEnemy(
            name='Skellington King',
            hp=30,
            damage=random.randint(5, 10),
            enemyType='boss',
            desc='''The King of Skeletons. He holds the power to command all Skellingtons.''',
            treasureClass=10,
            goldDrop=random.randint(10, 15),
            expDrop=10
        )

        skellingtonKing.addItemDrop(bones)
        skellingtonKing.addItemDrop(skullKey)

        enemies.append(skellington)
        enemies.append(skellingtonHound)
        # Boss of the Dungeon
        enemies.append(skellingtonKing)

    elif townChoice == 2:
        slimeSlime = Item.InitialiseItem(
            name='Slime',
            desc='slime collected from slimes ',
            effect=0,
            quest=True,
            cost=0
        )

        chickenflesh = Item.InitialiseItem(
            name='Chicken flesh',
            desc='collected from zombie chickens',
            effect=0,
            quest=True,
            cost=0
        )

        # name, hp, enemyType, desc, treasureClass, goldDrop, itemDrop, expDrop
        slime = InitialiseEnemy(
            name='Slime',
            hp=10,
            damage=random.randint(5, 10),
            enemyType='normal',
            desc='''its gross, its disgusting, its the slime!''',
            treasureClass=1,
            goldDrop=0,
            expDrop=2
        )
        slime.addItemDrop(slimeSlime)

        chickenZombie = InitialiseEnemy(
            name='Chicken zombie',
            hp=5,
            damage=random.randint(3, 7),
            enemyType='boss',
            desc='''what do you think, its a chicken zombie!''',
            treasureClass=1,
            goldDrop=0,
            expDrop=1
        )

        chickenZombie.addItemDrop(chickenflesh)

        enemies.append(slime)

        # Boss of the Dungeon
        enemies.append(chickenZombie)

    elif townChoice == 3:
        # Create quest items that the enemies will hold
        # name, desc, effect, quest, cost
        phantomSkulls = Item.InitialiseItem(
            name='Phantom Skulls',
            desc='Skulls collected from Phantoms',
            effect=0,
            quest=True,
            cost=0
        )

        SphinxHearts = Item.InitialiseItem(
            name='Sphinx Hearts',
            desc='This heart can be acquired by killing a Sphinx',
            effect=0,
            quest=True,
            cost=0
        )

        # name, hp, enemyType, desc, treasureClass, goldDrop, itemDrop, expDrop
        phantom = InitialiseEnemy(
            name='Phantom',
            hp=10,
            damage=random.randint(5, 10),
            enemyType='normal',
            desc='''This large flying creature will sure give you shivers!''',
            treasureClass=1,
            goldDrop=0,
            expDrop=2
        )

        phantom.addItemDrop(phantomSkulls)

        Sphinx = InitialiseEnemy(
            name='Sphinx',
            hp=5,
            damage=random.randint(3, 7),
            enemyType='normal',
            desc='''Tiny, cute, flying creatures... MORE LIKE OVERGROWN INSECTS!''',
            treasureClass=1,
            goldDrop=0,
            expDrop=1
        )

        Sphinx.addItemDrop(SphinxHearts)

        goblin = InitialiseEnemy(
            name='Goblin',
            hp=15,
            damage=random.randint(7, 12),
            enemyType='normal',
            desc='''Evil, green and fat elves! Stay away or DIE!''',
            treasureClass=1,
            goldDrop=0,
            expDrop=1
        )

        gobinMaster = InitialiseEnemy(
            name='Goblin Master',
            hp=40,
            damage=random.randint(16, 20),
            enemyType='boss',
            desc='''The Goblin Master ''',
            treasureClass=10,
            goldDrop=0,
            expDrop=10
        )

        enemies.append(phantom)
        enemies.append(Sphinx)
        enemies.append(goblin)

        # Boss of the Dungeon
        enemies.append(gobinMaster)

    elif townChoice == 4:
        bananas = Item.InitialiseItem(
            name='Bananas',
            desc='Bananas from the farm',
            effect=0,
            quest=True,
            cost=0
        )

        dragonscale = Item.InitialiseItem(
            name='Dragon Scale',
            desc='This scale can be aquired by killing the dragon',
            effect=0,
            quest=True,
            cost=0
        )

        abomination = InitialiseEnemy(
            name='Abomination',
            hp=10,
            damage=random.randint(5, 10),
            enemyType='normal',
            desc='''This ginormous worm will appear out of nowhere and kill you if your not ready.Its fovorite meal is bananas.''',
            treasureClass=1,
            goldDrop=0,
            expDrop=2
        )

        abomination.addItemDrop(bananas)

        ghost = InitialiseEnemy(
            name='Ghost',
            hp=5,
            damage=random.randint(3, 7),
            enemyType='normal',
            desc='''Invisible, scary and deadly it will eat you up in a second.''',
            treasureClass=1,
            goldDrop=0,
            expDrop=1
        )

        dragon = InitialiseEnemy(
            name='Dragon',
            hp=40,
            damage=random.randint(16, 20),
            enemyType='boss',
            desc='''The Dragon King ''',
            treasureClass=10,
            goldDrop=0,
            expDrop=10
        )

        dragon.addItemDrop(dragonscale)

        enemies.append(abomination)
        enemies.append(ghost)
        enemies.append(dragon)

    return enemies
