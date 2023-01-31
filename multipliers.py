def reduceScore(score, time, health):
    multiplier = (time / 100) + (health / 100)
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score
    # e.g: 60 * ((60 / 100) + (50 / 100)) = 66

def increaseScore(score, time, health):
    multiplier = 1 + ((time / 100) + (health / 100))
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score

def decideDamage(player, enemy):
    # perform an operation which chooses a random health value based on the defense of the player and the total health of the player:
    # enemyAttack = default damage
    # playerDefense = a percentage (below 100)
    # e.g. damage = (enemyAttack / playerHealth) * playerDefense
    # e.g. damageMultiplier = (5 / 100) * 0.5 = 0.025 damage to the player
    # damage = enemyAttack * damageMultiplier
    # finds the enemyAttack as a % of damageMultiplier
    enemyAttack = enemy.attack