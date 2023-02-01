from .enemy import Enemy
from random import randrange, randint
from ..multipliers import decideDamage
# attack and defense = randint(5, 50)
typesOfEnemies = {
    "Goblin": { "name": f"Goblin {randint(1, 1000)}", "strength": randint(5, 50), "defense": randint(5, 50) },
    "Bandit": { "name": f"Bandit {randint(1, 1000)}", "strength": randint(5, 50), "defense": randint(5, 50)},
    "Spiders": {"name": f"Spider {randint(1, 1000)}", "strength": randint(5, 50), "defense": randint(5, 50)},
    "Angry_Villager": {"name": f"Angry Villager {randint(1, 1000)}", "strength": randint(5, 50), "defense": randint(5, 50)}
}
generatedLoot = []
class Dungeon:
    def __init__(self, data):
        print(data)
        print(data.get("name"))
        self.name = data.get('name')
        self.type = data.get('type')
        self.passed = False # whether it's complete or not
        self.enemies = []
        self.loot = generatedLoot
    def spawnEnemies(self):
        for _ in range(3):
            print(_)
            enemyType = typesOfEnemies[[Enemy for Enemy in typesOfEnemies.values()]]
            print(enemyType)
            print(f"Spawning enemy of class: ")
            enemy = enemy()

    def getData(self):
        print(self.data)
        return self.data

    def battle(self, player, enemy):
        print("WIP")
        damage = decideDamage(player, enemy)
