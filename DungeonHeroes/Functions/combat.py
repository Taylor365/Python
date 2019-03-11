import time
from Functions import moveRoll


def combat(player, enemy):
    print()
    print('Enemy is: ')
    enemy.info()
    time.sleep(2)
    print()
    print()
    # We roll to see who goes first
    first = moveRoll.rollDice(player, enemy)
    if first == player:
        second = enemy
    else:
        second = player
    # Battle is over once hp reaches 0
    while not player.hp <= 0 and not enemy.hp <= 0:
        # First go attacks
        # Second go attacks
        # etc.
        # etc.
        # Player can attack, use skill, use item
        # Fight ends when hp <= 0
        damage = first.combatMoves()
        print()
        second.hp -= damage
        print(first.name + ' hit ' + second.name + ' for ' + str(damage) + ' damage.')
        time.sleep(1)
        damage = second.combatMoves()
        print()
        first.hp -= damage
        print(second.name + ' hit ' + first.name + ' for ' + str(damage) + ' damage.')
        time.sleep(1)
        print()
        print()
        time.sleep(1)
        print("player HP: " + str(player.hp))
        print("enemy HP: " + str(enemy.hp))
        time.sleep(1)

    if player.hp <= 0:
        winner = enemy
    else:
        winner = player
        print()
        print('The Enemy has been defeated!')
        print('You Won!')
        print()
        # When fight over: exp, gold, items dropped
        # Need to check if enemy has item
        player.addExp(enemy.expDrop)
        for item in enemy.itemDrop:
            player.addItem(item)
        player.addGold(enemy.goldDrop)
        time.sleep(5)
    # For now, all picked up - later we can choose which items to pick up

    return winner
