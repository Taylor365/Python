# Code for the Dungeon Masters Game
import time;
import random;

welcomeMessage = '''           
                    ...                            
                  ;::::;                           
                ;::::; :;                          
              ;:::::'   :;                         
              ;:::::;     ;.                        
            ,:::::'       ;           OOO\         
            ::::::;       ;          OOOOO\        
            ;:::::;       ;         OOOOOOOO       
            ,;::::::;     ;'         / OOOOOOO      
          ;:::::::::`. ,,,;.        /  / DOOOOOO    
        .';:::::::::::::::::;,     /  /     DOOOO   
      ,::::::;::::::;;;;::::;,   /  /        DOOO  
      ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
      :`:::::::`;::::::;;::: ;::#  /            DOOO
      ::`:::::::`;:::::::: ;::::# /              DOO
      `:`:::::::`;:::::: ;::::::#/               DOO
      :::`:::::::`;; ;:::::::::##                OO
      ::::`:::::::`;::::::::;:::#                OO
      `:::::`::::::::::::;'`:;::#                O 
        `:::::`::::::::;' /  / `:#                  
        ::::::`:::::;'  /  /   `#  
            ▓█████▄  ██░ ██ 
            ▒██▀ ██▌▓██░ ██▒
            ░██   █▌▒██▀▀██░
            ░▓█▄   ▌░▓█ ░██ 
            ░▒████▓ ░▓█▒░██▓
            ▒▒▓  ▒  ▒ ░░▒░▒
            ░ ▒  ▒  ▒ ░▒░ ░
            ░ ░  ░  ░  ░░ ░
              ░     ░  ░  ░
            ░              


        Welcome to DungeonHeroes           
   '''
chooseCharacterMenu = '''Please choose a character:
1 - Templar
2 - Wizard
3 - Archer
4 - Warrior'''

initialMenu = '''Choose your Faith:
1 - Begin
2 - Show Your Character Information
3 - Quit'''

GAMEOVER = False
TOWNSNOTCOMPLETED = [1, 2, 3, 4]

#******************************CLASSES****************************
class Character(object):
  def __init__(self, hp, mp, weight, gold, exp, desc, equipped):
    self.hp = hp
    self.mp = mp
    self.weight = weight      #Amount the character can carry. 
    self.skills = []          #Empty list of Skills for character.
    self.inventory = []       #Empty Inventory space for items.
    self.gold = gold          #Amount of current gold coins.
    self.exp = exp            #Experience gained.
    self.desc = desc          #Description of character.
    self.equipped = {
      "weaponEquipped": "",
      "shieldEquipped": ""
    }                         #Gear equipped dictionary

  #Here we create a method to print information.
  #Example: warrior.info()     
  def info(self):
    print ('****************************************************')
    print ('********~~~~Your Character Stats~~~~*****************')
    print ('****************************************************')
    print ('HP: ' + str(self.hp))
    print ('MP: ' + str(self.mp))
    print ('Max Weight: ' + str(self.weight))
    print ('Skills: [')
    for skill in self.skills:
      skill.infoShort()
    print (']')
    print ('Inventory: [')
    for item in self.inventory:
      item.infoShort()
    print (']')
    print ('Current Exp: ' + str(self.exp))
    print ('Current Gold: ' + str(self.gold))
    print ('Description: ' + self.desc)  
    print ('****************************************************')
    print ()

  def charIntro(self):
    print('"JUST WHAT THIS OLD KNIGHT WAS LOOKING FOR! >:)"')
    print ()

  def addSkill(self, newSkill):
    self.skills.append(newSkill)
    print('New Skill Gained! You can now use ' + newSkill.name + '!') 

  def addItem(self, newItem):
    self.inventory.append(newItem)
    print('Added ' + newItem.name + ' to your inventory.') 

  def addExp(self, newExp):
    self.exp += newExp
    print('You gained ' + str(newExp) + '! Total exp now ' + str(self.exp) + '.')

  def equipWeapon(self, weapon):
    self.equipped["weaponEquipped"] = weapon.name
    print('Equipped ' + weapon.name + '.') 

  def equipShield(self, shield):
    self.equipped["shieldEquipped"] = shield.name
    print('Equipped ' + shield.name + '.') 

  #Character Turns - attack, use skill, use item
  def attack(self):
    #Do attack
    print('attack') 
  
  def useSkill(self):
    #Do attack
    print('use skill')
  
  def useItem(self):
    #Do attack
    print('use item')

class Town(object):
  def __init__(self, name, dungeon, shop, npcs, quests, desc):
    self.name = name            #Name of town
    self.dungeon = dungeon      #The town dungeon
    self.shop = shop            #The town shop
    self.npcs = []              #Empty list of NPCs in town.
    self.quests = []            #Empty list of Quests in town.
    self.desc = desc            #Description of the town.

  #Here we create a method to print information.
  #Example: town.info()     
  def info(self):
    print ('****************************************************')
    print ('********~~~~Welcome to ' + self.name + '~~~~*****************')
    print ('****************************************************')
    print (self.desc)

  def addNpc(self, newNPC):
    self.npcs.append(newNPC)

  def addQuest(self, newQuest):
    self.quests.append(newQuest)

  def addShop(self, newShop):
    self.shop = newShop

  def addDungeon(self, newDungeon):
    self.dungeon = newDungeon

class Enemy(object):
  def __init__(self, hp, enemyType, desc, treasureClass, goldDrop, itemDrop, expDrop):
    self.hp = hp
    self.skills = []                    #List of enemy Skills
    self.enemyType = enemyType          #Type of enemy, normal, boss, etc.
    self.desc = desc                    #Description of enemy
    self.treasureClass = treasureClass  #What level of item they can drop
    self.goldDrop = goldDrop            #Gold to drop
    self.itemDrop = itemDrop            #Items to drop
    self.expDrop = expDrop              #Experience to give

  def info(self): 
    print ('HP: ' + self.hp)
    print ('Skills: ' + self.skills)
    print ('Type: ' + self.enemyType)
    print ('Description: ' + self.desc)

  #Enemy Turns - attack, use skill
  def attack(self):
    #Do attack
    print('attack') 
  
  def useSkill(self):
    #Do attack
    print('use skill')

class Weapon(object):
  def __init__(self, name, damage, weaponType, desc, weight): #Constructor
    self.name = name
    self.damage = damage
    self.weaponType = weaponType  #Axe, Bow, Sword, etc. 
    self.desc = desc              #Description of weapon
    self.weight = weight          #How much it weighs
        
  #Here we create a method to print information.
  #Example: rustySword.info()     
  def info(self): 
    print ('Name: ' + self.name)
    print ('Damage: ' + str(self.damage))
    print ('Type: ' + self.weaponType)
    print ('Weight: ' + str(self.weight))
    print ('Description: ' + self.desc)

  def infoShort(self): 
    print (self.name)

class Shield(object):
  def __init__(self, name, blockChance, shieldType, desc, weight):
    self.name = name
    self.blockChance = blockChance  #Chance to block attack
    self.shieldType = shieldType    #Round, Kite, Tower, etc. 
    self.desc = desc                #Description of shield
    self.weight = weight            #How much it weighs
        
  #Here we create a method to print information.
  #Example: woodenShield.info()     
  def info(self): 
    print ('Name: ' + self.name)
    print ('Block Chance: ' + str(self.blockChance))
    print ('Type: ' + self.shieldType)
    print ('Weight: ' + str(self.weight))
    print ('Description: ' + self.desc)

  def infoShort(self): 
    print (self.name)

class Skill(object):
  def __init__(self, name, damage, mpReq, expReq, desc): #Constructor
    self.name = name
    self.damage = damage
    self.mpReq = mpReq        #How much MP it requires to use
    self.expReq = expReq      #How much Exp is required to unlock
    self.desc = desc          #Description of the skill
         
  def info(self): 
    print ('Name: ' + self.name)
    print ('Damage : ' + str(self.damage))
    print ('MP: ' + str(self.mpReq))
    print ('Experience required to unlock: ' + str(self.expReq))
    print ('Description: ' + self.desc)
    print ()

  def infoShort(self): 
    print (self.name)

class Npc(object):
  #Create NPC
  def __init__(self, name, quest, shopKeep, desc): #Constructor
    self.name = name
    self.quest = quest            #Check if they have a quest
    self.shopKeep = shopKeep      #Check if they are shopkeeper
    self.desc = desc              #Description of the Npc
         
  def info(self): 
    print ('Name: ' + self.name)
    print ('Description: ' + self.desc)
    print ()

  def infoShort(self): 
    print (self.name)

class Quest(object):
  def __init__(self, name, desc, trigger, reqToFinish, reward, finished): #Constructor
    self.name = name
    self.desc = desc      
    self.trigger = trigger    #This is what starts the Q
    self.reqToFinish = reqToFinish  #Required to Finish
    self.reward = reward            #Reward for Q
    self.finished = finished        #If Done

  def info(self): 
    print ('Name: ' + self.name)
    print ('Description: ' + self.desc)
    print ('Required: ' + self.desc)
    print ('Reward: ' + self.desc)
    print ()

  def infoShort(self): 
    print (self.name)

class Shop(object):
  def __init__(self, name, desc, inventory, gold, shopkeeper):
    self.name = name
    self.desc = desc              #Description
    self.inventory = []           #Shop Items
    self.gold = gold              #Gold in shop
    self.shopkeeper = shopkeeper  #Shopkeeper
         
  def info(self): 
    print ('Name: ' + self.name)
    print ('Description: ' + self.desc)
    print ('Inventory: ' + self.inventory)
    print ('Gold: ' + self.gold)
    print ('Shopkeeper: ' + self.shopkeeper)
    print ()

  def infoShort(self): 
    print (self.name)

class Dungeon(object):
  #Create Dungeon
  def __init__(self, name, enemyTypes, enemyAmount, secretItem, desc, cleared): #Constructor
    self.name = name
    self.enemyTypes = []            #Contains the enemyTypes
    self.enemyAmount = enemyAmount  #The amount of enemies
    self.secretItem = secretItem    #The secret Item in the dungeon
    self.desc = desc                #Description of the Dungeon
    self.cleared = cleared           #Check if finished
         
  def info(self): 
    print ('Name: ' + self.name)
    print ('Description: ' + self.desc)
    print ()

  def infoShort(self): 
    print (self.name)

#******************************CLASSES****************************

#***************************CREATE METHODS*************************

def createCharacter(characterChoice):
    if characterChoice == '1':

      #Creating the Templar
      templar = Character(
        hp = 100,
        mp = 50,
        weight = 100,
        gold = 0,
        exp = 0,
        desc = '''An old experienced Knight left over from the Crusades. His grey and white hair, scars, and steely gaze are all that remain. He wears an eye patch to cover the hole were his eye used to be, along with rusted armor, a shield that embraces the red and white colours of the Knights Templar...''',
        equipped = {}
      )

      #Creating Skills
      bash = Skill(
        'Bash', 6, 5, 0, 'Bash enemy with shield.')
      divineTouch = Skill(
        'Divine Touch', 0, 20, 40, 'Heals the Templar to full HP. Can only be used once!')
      cluckVoience = Skill(
        'Cluck Voience', 0, 50, 100, 'Turns an enemy into a loveable chicken. Only works on normal enemies.')

      #Add Skills to Character
      templar.addSkill(bash)

      #Creating Starting Gear
      rustySword = Weapon(
          'Rusty Sword', 
          1, 
          'Short Sword',
          'An old rusted sword. This sword must be hundreds of years old.', 
          10)
      woodenShield = Shield(
        'Old Wooden Shield', 10,
        'Kite Shield',
        'An old wooden shield in the shape of a kite. Used mostly by Knights.',
        20)
      
      #Adding starting gear to Inventory
      templar.addItem(rustySword)
      templar.addItem(woodenShield)

      return templar

    elif characterChoice == '2':
      #do create
      wizard = Character(
        hp = 50,
        mp = 100,
        weight = 70,
        gold = 0,
        exp = 0,
        desc = '''He is an old man with limitless amount of magic power from a difrent land. He was the most powerfull out of his kind and now he stands here ready for what what will come to him...'''
      )

      #Creating Skills
      #name, damage, mpReq, expReq, desc
      fireball = Skill(
        'Fireball', 6, 10, 0, 'Shoots a ball of fire at the enemy.')
      splitIllusion = Skill(
        'Split Ilusion', 0, 20, 40, 'The wizard creates a decoy of himself to shield attacks.')
      soulsavior = Skill(
        'Soulsavior', 0, 50, 100, 'Kills enemy and heals wizard up to full health.')

      #Add Skills to Character
      wizard.addSkill(fireball)
      wizard.addSkill(splitIllusion)
      wizard.addSkill(soulsavior)

      #Creating Starting Gear
      #name, damage, weaponType, desc, weight
      longstick = Weapon(
          'longstick', 
          1, 
          'staff',
          'A simple stick off a tree.', 
          10)
      book = Shield(
        'Book of Skellia', 20,
        'Book Shield',
        'An old book. The pages are made from crystal. The words spoken protect the user.',
        5)
      
      #Adding starting gear to Inventory
      wizard.addItem(longstick)
      wizard.addItem(woodenShield)

      return wizard 
    elif characterChoice == '3':
      archer = Character(
        hp = 70, 
        mp = 70, 
        weight = 60, 
        gold = 0, 
        exp = 0, 
        desc = '''A brave young Archer left over from the battles. He travels mystically around. With him near you, you really would want to turn around and run. Every battle makes him stronger, smarter and last but not least, it makes him want more...'''
      )
      #Creating Skills
      #name, damage, mpReq, expReq, desc
      freezeArrow = Skill(
        'Freeze Arrow', 0, 10, 0, 'Freeze the enemy with a Frozen Arrow!')
      powerDraw = Skill(
        'Power Draw', 1, 5, 40, 'Charge up and fire a thunderous arrow!')
      shadowCloak = Skill(
        'Shadow Cloak', 0, 40, 100, 'Vanish to be unseen for 2 turns!')
      #Add Skills to Character
      archer.addSkill(freezeArrow)
      archer.addSkill(powerDraw)
      archer.addSkill(shadowCloak)
      #Creating Starting Gear
      oldBow = Weapon(
          'Old Bow', 
          2,
          'Bow',
          'An old rusted bow. This bow must be hundreds or thousands of years old.',10)
      rustedDagger = Weapon(
        'Rusted Dagger', 
        5,
        'Dagger',
        'An old rusted dagger. People say not one were killed with this rusted weapon.',
        20)
      #Adding starting gear to Inventory
      archer.addItem(oldBow)
      archer.addItem(rustedDagger)

      return archer 
    elif characterChoice == '4':
      warrior = Character(
        hp = 120,
        mp = 50,
        weight = 120,
        gold = 0,
        exp = 0,
        desc = '''A brave young warrior out to fight the whole world. He was sent from the king to do all types of quests. He is a very good damage dealer but is a bit out of shape, through the story he might become fitter, you might even call him OP!'''
      )    
      # name, damage, mpReq, expReq, desc
      shieldSaviour = Skill(
        'Shield Saviour', 0, 15, 0, 'The warrior raises his arms to create a shield infront of him.')
      chargeAttack = Skill(
        'Charge Attack', 5, 10, 40, 'The warrior charges at his enemy doing extra damage.')
      warCry = Skill(
        'War Cry', 0, 40, 100, 'The warrior bellows his voice causing enemies to turn against each other.')

      #Add Skills to Character
      warrior.addSkill(shieldSaviour)
      warrior.addSkill(chargeAttack)
      warrior.addSkill(warCry)

      rustyAxe = Weapon(
          'Rusty Axe', 
          1, 
          'Axe',
          'An old rusty axe .', 
          10)
      copperShield = Shield(
        'Copper Shield', 10,
        'Coppe',
        'An old metally shield.',
        20)
      
      #Adding starting gear to Inventory
      warrior.addItem(rustyAxe)
      warrior.addItem(copper)

      return warrior

def createTown(townChoice):
    if townChoice == 1:

      #Creating the Town
      #name, dungeon, shop, npcs, quests, desc
      cardium = Town(
        name = 'Cardium',
          #name, enemyTypes, enemyAmount, quest, secretItem, desc, cleared
        dungeon = None,          
        shop = None,
        npcs = [],
        quests = [],
        desc = '''A once thriving town, now scarce and barren. In the center stand a huge Monastery with a spiked tower that holds a clock and bell. The clock doesn't seem to work and dark clouds surround the big structure. There is also a few houses along the road with a shop.'''
      )

      #Creating Dungeon
      #name, enemyTypes, enemyAmount, secretItem, desc, cleared
      monastery = Dungeon('The Monastery', 
      None,
      5, 
      #name, damage, weaponType, desc, weight
      Weapon('Secret', 5, 'Axe', 'Tis secret', 50),
      '''An old stone monastery. It gives a spooky vibe...''',
      False
      )

      #Add Dungeon to Town
      cardium.addDungeon(monastery)

      #Creating Quests
      #name, desc, trigger, reqToFinish, reward, finished
      quest1 = Quest('Bones',
      '''Asha requires bones for her potion. Collect 5 bones from skeletons in the Monestary.''',
      1, 1, 1,
      False)
      quest2 = Quest('Greed',
      '''Grizzly's greed knows no bounds. He has found an extra special weapon you could use, but requires the coin! Collect 50 gold and Grizzly will hand it over...''',
      1, 1, 1,
      False)
      quest3 = Quest('From The Ashes',
      '''Clear out the Monastery off skellingtons and bring life back to the town!''',
      1, 1, 1,
      False)

      #Creating NPCs
      #name, quest, shopKeep, desc
      asha = Npc(
        'Asha', quest1, False, 'An old sorceress. She has lived in Cardium her entire life.')
      grizzly = Npc(
        'Grizzly', quest2, True, 'A greedy shopkeeper. Only interested if you have coin.')
      kretian = Npc(
        'Kretian', quest3, False, 'An old mercenary. He is blind but nothing escapes him.')

      #Add Npcs to Town
      cardium.addNpc(asha)
      cardium.addNpc(grizzly)
      cardium.addNpc(kretian)
      
      #name, desc, inventory, gold, shopkeeper
      grizzlyShop = Shop('Greedy Grizzlies', 
        'A dirty run-down shack. Not much here but old gear.',
        [],
        100,
        grizzly)

      #Add Shop to Town
      cardium.addShop(grizzlyShop)
      
      #Adding quests to Town
      cardium.addQuest(quest1)
      cardium.addQuest(quest2)
      cardium.addQuest(quest3)

      return cardium

    elif townChoice == 2:
      #do create
      HP = 0
    elif townChoice == 3:
      #do create
      HP = 0
    elif townChoice == 4:
      #do create
      HP = 0    

#***************************CREATE METHODS*************************

def rollDice(x, y):
  return random.randint(x, y)

while(GAMEOVER == False):
  #Do game
  print(welcomeMessage)
  time.sleep(5)
  for i in range(4):
    print()
  print(chooseCharacterMenu)
  print ()
  characterChoice = input('Choose your Character: ')
  character = createCharacter(characterChoice)
  print()
  while(GAMEOVER == False):
    print(initialMenu)
    #print("I have {0} apples and {1} pears".format(input(), input()))
    print ()
    initialChoice = input('Make your choice: ')
    print ()
    if initialChoice == '1':   
      print ('***************************~~~~Prologue~~~~***************************')
      print('You come to a signpost at the end of a long, dusty road. It reads, "Turn back. Foul creatures have taken over the Monastery. Some brave townsfolk take shelter in the town, but I would call them MAD!". Press ENTER to continue...')
      temp = input()
      print('Your gaze rises to the skies..')
      for i in range(4):
        time.sleep(1.25)
        print('.')
      character.charIntro()
      time.sleep(2)
      print('You press onwards to the town...')
      path = 'dirtPath'
      time.sleep(3)
      print ()
      print ()
      while(character.hp > 0):
        #PATH CHOICE - A TOWN (30%) OR DIRT ROAD(70%)

        # THE DIRT PATH CODE
        while(path == 'dirtPath'):
          pathChance = rollDice(0, 10)
          print('Path = ' + str(pathChance))
          time.sleep(2)
          if pathChance > 3:
            print('The winds howl. You come across another long dusty path.....Press ENTER to continue')
            temp = input()
            print()
            print()
            battleChance = rollDice(0, 10)
            print('Battle Chance = ' + str(battleChance))
            if battleChance > 5:
              print('Do Battle!')
              print('Fight fight fight!')
              temp = input('Press ENTER to continue')
          else:
            print("You've come across a town!!")
            time.sleep(2)
            path = 'town'

        townFinished = False
        # THE TOWN CODE
        while(path == 'town' and townFinished == False):
          #Pick random town of the 4
          townToVisit = 1 #randomTownPicker()
          town = createTown(1)
          time.sleep(2)
          print()
          town.info()
          print()
          print('1 - Visit ' + town.shop.name + ' Shop')
          print('2 - Visit ' + town.npcs[0].name + "'s house")
          print('3 - Enter the ' + town.dungeon.name)
          print()
          townChoice = input('Make your choice: ')

          if townChoice == '1':
            #Do shop
            print('Welcome to ' + town.shop.name)
            print()
            print()#ShopKeeper greeting
            print()#ShopKeeper Menu
            input('Press ENTER to continue: ')
          elif townChoice == '2':
            #Do shop
            print('You are now in ' + town.npcs[0].name + "'s house")
            print()
            print()#Npc greeting
            print()#Npc Menu
            input('Press ENTER to continue: ')
          elif townChoice == '3':
            #Do shop
            print('Welcome to the darkness of ' + town.dungeon.name)
            print()
            print('Do Battle!')
            print('Fight fight fight!')
            print()
            print()
            input('Press ENTER to continue: ')
            time.sleep(3)

          questScore = 0
          for quest in town.quests: 
            quest.finished = True
            if quest.finished == True:
              questScore += 1
          
          if questScore == 3:
            townFinished = True            
            print()
            print()
            print('''You have completed all quests in this town. Onwards to the next! Somewhere else might be in need of help...''')
            path = 'dirtPath'
            TOWNSNOTCOMPLETED.remove(townToVisit)
            print()
            if TOWNSNOTCOMPLETED:
              print('Towns left to do: ' + str(TOWNSNOTCOMPLETED))
            print()
            print()
            
        #character.hp = 0
      
      print ('THE END :)))))))')
      GAMEOVER = True
    elif initialChoice == '2':   
      character.info()
    elif initialChoice == '3':   
      print ('Leaving so soon?... :(')
      GAMEOVER = True


