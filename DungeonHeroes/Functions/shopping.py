

def shopping(player, shop):
    shopping = True

    while shopping == True:
        shoppingchoice = input ('1- Buy\n2- Sell\n3- Finish')
        if shoppingchoice == '1':
            print ('check shop inventory')
            if len(shop.inventory) > 0:
                print ('show items')
                for item in shop.inventory:
                    item.infoShort()
                buychoice = input('choose an item to buy or enter 0 to go back')
                if buychoice == 0:
                    shoppingchoice = 0
                else:
                    exists = any(w for w in shop.inventory if w.name == buychoice)
                    if exists:
                        for item in shop.inventory:
                            if item.name == buychoice:
                                if player.gold < 5:
                                    shop.inventory.remove(item)
                                    shop.gold += 5
                                else:
                                    print ('not enough gold')
                    else:
                        print("That item doesn't exist!")
            else:
                print ('go back to menue')
        while shoppingchoice == '2':
            print('check player inventory')
            len(player.inventory)
            if len(player.inventory) <= 0:
                print ('Go back to menue')
            else:
                print('player inventory')
                for item in player.inventory:
                    item.infoShort()
                print('choose an item to sell or enter 0 to go back')
                sellchoice = input('Item to sell: ')
                if sellchoice == '0':
                    shoppingchoice = 0
                else:
                    exists = any(w for w in player.inventory if w.name == sellchoice)
                    if exists:
                        for item in player.inventory:
                            if item.name == sellchoice:
                                player.inventory.remove(item)
                                player.gold += 5
                    else:
                        print("That weapon doesn't exist!")
        if shoppingchoice == '3':
            shopping = False