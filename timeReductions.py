def reduce(time, health):
    multiplier = (time / 100) + (health / 100)
    score_reduction = time * multiplier
    
    # e.g: 60 * ((60 / 100) + (50 / 100)) = 66
