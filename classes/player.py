from .character import Character
from ..multipliers import increaseScore
class Player(Character):
    def __init__(self, data):
        super().__init__(self, data)


    def encounterEnemy(self, enemy):
        self.currentDungeon = enemy.dungeon
    def defeatEnemy(self, enemy):
        increaseScore(self.get('score'))

    def beatDungeon(self, dungeon):
        self.currentDungeon = False
        self.inventory.append(dungeon.loot)

