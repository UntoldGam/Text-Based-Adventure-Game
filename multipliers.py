def reduceScore(score, time, health):
    multiplier = (time / 100) + (health / 100)
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score

def increaseScore(score, time, health):
    multiplier = 1 + ((time / 100) + (health / 100))
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score

def decideDamage(player, enemy):
    # enemyAttack = default damage
    # playerDefense = a percentage (below 100)
    # e.g. damage = (enemyAttack / playerHealth) * playerDefense
    # e.g. damageMultiplier = (5 / 100) * 0.5 = 0.025 damage to the player
    # damage = enemyAttack * damageMultiplier
    # finds the enemyAttack as a % of damageMultiplier
    enemyAttack = enemy.attack
    playerDefense = player.defense
    playerHealth = player.health

    damageMultiplier = (enemyAttack / playerHealth) * playerDefense
    damage = enemyAttack * damageMultiplier
    return damage