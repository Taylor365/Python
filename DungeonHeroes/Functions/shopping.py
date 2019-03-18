def start(player, shop):
    shoppingOver = False

    while not shoppingOver:
        shoppingchoice = input('1 - Buy\n2 - Sell\n3 - Finish\n\nSelect Your Choice: ')
        if shoppingchoice == '1':
            if len(shop.inventory) > 0:
                shop.buychat()
                print('\nThe shop inventory:')
                shop.infoInventory()
                print('\nChoose an item to sell or enter 0 to go back.')
                buychoice = input('Item to buy: ')
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
                                    print('Not enough gold')
                    else:
                        print("That item doesn't exist!")
            else:
                print('\nThis shop has no items! :O\n')
        while shoppingchoice == '2':
            len(player.inventory)
            if len(player.inventory) <= 0:
                print('\nPlayer has nothing in their inventory!\n')
            else:
                shop.sellchat()
                print('\nItems you can sell:')
                for item in player.inventory:
                    item.infoShort()
                print('\nChoose an item to sell or enter 0 to go back.')
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
                                print('You traded the ' + item.name + ' and received 5 gold! ')
                                print('You now have ' + str(player.gold) + '.')
                    else:
                        print("That weapon doesn't exist!")
        if shoppingchoice == '3':
            shop.leavechat()
            shoppingOver = True
