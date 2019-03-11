from Functions import randomRoll


def rollDice(player, enemy):
    playerRoll = randomRoll.rollDice(1, 10)
    enemyRoll = randomRoll.rollDice(1, 10)
    first = None
    while first == None:
        if enemyRoll > playerRoll:
            first = enemy
        elif enemyRoll < playerRoll:
            first = player

    return first
