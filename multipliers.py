"""
def reduceScore(score, time, health):
    multiplier = 1 - (time / 100) + (health / 100)
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score

def increaseScore(score, time, health):
    multiplier = 1 + ((time / 100) + (health / 100))
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score
"""

def decideDamage(player, enemy, bonus=False):
    # enemyAttack = default damage (10)
    # playerDefense = a percentage (below 100)
    # e.g. damage = (enemyAttack / playerHealth) * playerDefense
    # e.g. damageMultiplier = (5 / 100) * 0.5 = 0.025 damage to the player
    # damage = enemyAttack * damageMultiplier
    # finds the enemyAttack as a % of damageMultiplier
    enemyAttack = enemy.attack
    enemyDefense = enemy.defense
    playerDefense = player.data.get("defense")
    playerHealth = player.data.get("attack")

    damageMultiplier = (enemyAttack / enemyDefense) * (playerDefense / 10)  
    damage = enemyAttack / damageMultiplier
    #print(damageMultiplier, damage)
    if bonus:
        damage = damage * bonus
        #print(damage)
        return damage
    else:
        return damage