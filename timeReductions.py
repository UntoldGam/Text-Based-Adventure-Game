def reduce(score, time, health):
    multiplier = (time / 100) + (health / 100)
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score
    # e.g: 60 * ((60 / 100) + (50 / 100)) = 66

def increase(score, time, health):
    multiplier = 1 + ((time / 100) + (health / 100))
    final_multiplier = time * multiplier
    score *= final_multiplier
    return score