from .character import Character
from ..multipliers import increaseScore
class User(Character):
    def __init__(self, data):
        super().__init__(self, data)
        self.name = data.get('username')
        self.health = 100 # default health
        self.score = 0 # default score
        self.passed_locations = [] # default passed locations

    def encounterEnemy(self, enemy):
        self.currentDungeon = enemy.dungeon
    def defeatEnemy(self, enemy):
        increaseScore(self.score)

    def beatDungeon(self, dungeon):
        

