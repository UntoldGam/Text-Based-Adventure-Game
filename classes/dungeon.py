class Dungeon:
    def __init__(self, data):
        print(data)
        print(data.get("name"))
        self.name = data.get('name')
        self.type = data.get('type')
        self.passed = False # whether it's complete or not
    def getData(self):
        print(self.data)
        return self.data

    def battle(self):
        # perform an operation which chooses a random health value based on the defense of the player and the total health of the player:
        # enemyAttack = default damage
        # playerDefense = a percentage (below 100)
        # e.g. damage = (enemyAttack / playerHealth) * playerDefense
        # e.g. damageMultiplier = (5 / 100) * 0.5 = 0.025 damage to the player
        # damage = enemyAttack * damageMultiplier
        print("WIP")

    def complete(self):
        self.passed = True