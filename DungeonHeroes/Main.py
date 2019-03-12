import time
import random
from Classes import Weapon, Shield, Character, Town
from Functions import randomRoll, combat, NPCInteraction


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

isgameover = False
townsnotcompleted = [1, 2, 3, 4]
player = None

while (isgameover == False):
    print(welcomeMessage)
    time.sleep(5)
    for i in range(4):
        print()
    print(chooseCharacterMenu)
    print()
    characterChoice = input('Choose your Character: ')
    player = Character.create(characterChoice)
    print()
    while (isgameover == False):
        print(initialMenu)
        print()
        initialChoice = input('Make your choice: ')
        print()
        if initialChoice == '1':
            print('***************************~~~~Prologue~~~~***************************')
            print('''You come to a signpost at the end of a long, dusty road. 
                It reads, "Turn back. Foul creatures have taken over this land. 
                Some brave townsfolk take shelter in the town, but I would call them MAD!". 
                Press ENTER to continue...''')
            temp = input()
            print('Your gaze rises to the skies..')
            for i in range(4):
                time.sleep(1.25)
                print('.')
            player.charIntro(characterChoice)
            time.sleep(2)
            print('You press onwards to the town...')
            path = 'dirtPath'
            time.sleep(3)
            print()
            print()

            GAMEFINISHED = False
            while (GAMEFINISHED != True):
                # PATH CHOICE - A TOWN (30%) OR DIRT ROAD(70%)

                # THE DIRT PATH CODE
                while (path == 'dirtPath'):
                    pathChance = randomRoll.rollDice(0, 10)
                    # print('Path = ' + str(pathChance))
                    time.sleep(2)
                    # TODO - Rework the random encounter between towns
                    if pathChance == 11:
                        print('The winds howl. You come across another long dusty path.....Press ENTER to continue')
                        temp = input()
                        print()
                        print()
                        battleChance = randomRoll.rollDice(0, 10)
                        print('Battle Chance = ' + str(battleChance))
                        if battleChance > 5:
                            print('Do Battle!')
                            # Roll dice for turns
                            # turn 1 - attack/defend/use item/skill + enemy turn - attack
                            # turn 2 - attack/defend/use item
                            # turn 3 - attack/defend/use item
                            # etc
                            # When enemy hp => 0 give rewards to player (exp, gold, item)
                            print('Fight fight fight!')
                            temp = input('Press ENTER to continue')
                    else:
                        print("You've come across a town!!")
                        print()
                        print()
                        player.charTown(characterChoice)
                        time.sleep(2)
                        path = 'town'

                # Pick random town of the 4
                townToVisit = random.choice(townsnotcompleted)

                town = Town.createTown(townToVisit)
                townFinished = False
                # THE TOWN CODE
                while (path == 'town' and townFinished == False and GAMEFINISHED == False):
                    time.sleep(2)
                    print()
                    town.info()
                    print()
                    print('1 - Visit ' + town.shop.name + ' Shop')
                    print('2 - Visit ' + town.npcs[0].name + "'s house")
                    if town.dungeon.cleared == False:
                        print('3 - Enter Dungeon: ' + town.dungeon.name)
                    else:
                        print('4 - The Dungeon is complete - Move on to the Next Town?')

                    print()
                    townChoice = input('Make your choice: ')
                    time.sleep(2)
                    print()

                    if townChoice == '1':
                        # Do shop
                        print('Welcome to ' + town.shop.name)
                        print()
                        print()  # ShopKeeper greeting
                        NPCInteraction.interaction(town.shop.shopkeeper, town, player)
                    elif townChoice == '2':
                        # Do shop
                        print('You are now in ' + town.npcs[0].name + "'s house")
                        print()
                        print()  # Npc greeting
                        NPCInteraction.interaction(town.npcs[0], town, player)
                    elif townChoice == '3' and town.dungeon.cleared == False:
                        # Do shop
                        print('Welcome to the darkness of ' + town.dungeon.name)
                        print()

                        # Gear Equipping
                        if (len(player.inventory) < 1):
                            print('You have nothing in your inventory!! Uh Oh!')
                        else:
                            gearChoice = '1'
                            time.sleep(1)
                            while gearChoice == '1':
                                print('\nWould you like to equip new Gear?')

                                # Ternary Condition USED!!
                                printCurrentWeapon = player.equipped['weaponEquipped'].name \
                                if player.equipped['weaponEquipped'] != None else 'Nothing Equipped'
                                printCurrentShield = player.equipped['shieldEquipped'].name \
                                if player.equipped['shieldEquipped'] != None else 'Nothing Equipped'

                                print(
                                    'Current weapon is ' + printCurrentWeapon + '\nCurrent shield is ' + printCurrentShield)
                                print('\n1 - Equip new Gear\n2 - Keep current Gear')
                                gearChoice = input('Your choice: ')
                                if (gearChoice == '1'):
                                    print('\nWhich weapon would you like to equip?\n')
                                    for item in player.inventory:
                                        if type(item) is Weapon:
                                            print(item.name)
                                    weaponChoice = input('Type the weapon to equip it: ')
                                    exists = any(w for w in player.inventory if w.name == weaponChoice)
                                    if exists:
                                        for item in player.inventory:
                                            if item.name == weaponChoice:
                                                player.equipGear(item, 'weapon')
                                    else:
                                        print("That weapon doesn't exist!")

                                    print('\nWhich shield would you like to equip?\n')
                                    for item in player.inventory:
                                        if type(item) is Shield:
                                            print(item.name)
                                    shieldChoice = input('Type the shield to equip it: ')
                                    exists = any(w for w in player.inventory if w.name == shieldChoice)
                                    if exists:
                                        for item in player.inventory:
                                            if item.name == shieldChoice:
                                                player.equipGear(item, 'shield')
                                    else:
                                        print("That shield doesn't exist!")

                        time.sleep(2)
                        print()
                        # While normal enemies exist, fight them
                        enemies = town.dungeon.dungeonEnemies
                        while any(x for x in enemies if x.enemyType == 'normal'):
                            enemyCount = len(enemies) - 1
                            enemy = enemies[random.randint(0, enemyCount)]
                            if enemy.enemyType == 'normal':
                                battle = combat(player, enemy)
                                if battle == player:
                                    enemies.remove(enemy)
                                    player.info()
                                if battle == enemy:
                                    print('You Lose')
                                    isgameover = True
                                    GAMEFINISHED = True

                        # FIGHT THE BOSS + Back to town
                        if (isgameover != True):
                            print()
                            print()
                            print('NO MORE NORMAL ENEMIES, TIME FOR THE BOSS! :o')
                            time.sleep(3)
                            print()
                            print()
                            print()
                            enemy = enemies[0]
                            battle = combat(player, enemy)
                            if battle == player:
                                print('You Beat the Boss and the Dungeon!! The spoils are yours! :)')
                                enemies.remove(enemy)
                                print()
                                player.info()
                                print()
                                time.sleep(5)
                                town.dungeon.cleared = True
                                input('Press ENTER to head back to Town: ')
                            if battle == enemy:
                                print("You have Fallen!..... :'(")
                                isgameover = True
                                GAMEFINISHED = True

                            time.sleep(3)

                            questScore = 0
                            for quest in town.quests:
                                # quest.finished = True
                                if quest.finished == True:
                                    questScore += 1

                            if questScore == 3:
                                print('huh?')

                    elif townChoice == '4':
                        townFinished = True
                        print()
                        print()
                        print(
                            '''You have completed all quests in this town. Onwards to the next! Somewhere else might be in need of help...''')
                        path = 'dirtPath'
                        townsnotcompleted.remove(townToVisit)
                        print()
                        if townsnotcompleted:
                            print('Towns left to do: ' + str(townsnotcompleted))
                        else:
                            print('You win! THE END :)))))))')
                            isgameover = True
                            GAMEFINISHED = True
                        print()
                        print()

        elif initialChoice == '2':
            player.info()
        elif initialChoice == '3':
            print('Leaving so soon?... :(')
            isgameover = True

if player.hp <= 0:
    gameOverMessage = '''


    ▄████  ▄▄▄       ███▄ ▄███▓▓█████  ▒█████   ██▒   █▓▓█████  ██▀███  
  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
  ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
  ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
  ░ ░   ░   ░   ▒   ░      ░      ░   ░ ░ ░ ▒       ░░     ░     ░░   ░ 
        ░       ░  ░       ░      ░  ░    ░ ░        ░     ░  ░   ░     
                                                    ░                   

  '''
else:
    gameOverMessage = '''


  ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ██╗██╗██╗      ██╗        ██╗ 
  ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗██║██║██║     ██╔╝██╗     ╚██╗
  ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝██║██║██║    ██╔╝ ╚═╝█████╗██║
  ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝    ╚██╗ ██╗╚════╝██║
  ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║██╗██╗██╗     ╚██╗╚═╝     ██╔╝
  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝      ╚═╝        ╚═╝ 

  '''

print(gameOverMessage)
