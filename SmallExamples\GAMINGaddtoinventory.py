# adding to inventory for game

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):   #length of dragonLoot list = 5
        inventory.setdefault(addedItems[i],0)  #Add any items not already in inventory and set them to 0. (Ruby, Dagger)
        inventory[addedItems[i]]=inventory[addedItems[i]]+1  #For each item in dragonLoot, add 1. (3 coins, 1 dagger, 1 Ruby)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)


displayInventory(inv)


#    for i in range(len(addedItems)):
#          inventory.setdefault(addedItems[i],0)
#          inventory[addedItems[i]]=inventory[addedItems[i]]+1
