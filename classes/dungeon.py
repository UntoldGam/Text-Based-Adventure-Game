from random import randrange, randint, sample
from fileHandler import testDump
from .enemy import Enemy
from json import dumps
types = ["Ruin", "Cave", "Ravine", "Bandit Camp"]
items = ["Dagger", "Clock", "Apple", "Orange"]
enemies = [
    Enemy({ "name": "Goblin"}),
    Enemy({"name": "Bandit"}), 
    Enemy({"name": "Spider"}),
    Enemy({ "name": "Ghost"}),
    Enemy({ "name": "Troll" }),
]

loot = {
 "x2 Attack Boost": { "name": "x2 Attack Boost", "id": "2_attack"},
 "x2 Defense Boost": { "name": "x2 Defense Boost", "id": "2_defense"},
 "x2 Health Boost": { "name": "x2 Health Boost", "id": "2_health"},    
}
def generateLoot():
  dungeonLoot = []
  for _ in range(0, 3):
    lootItem = sample(set(loot.keys()), 1)[0]
    
    #lootItem = lootItem[0]
    #print(lootItem, type(lootItem))
    lootItem = loot.get(lootItem)
    #print(lootItem, type(lootItem))
    dungeonLoot.append(lootItem)
    #dungeonLoot.append(loot[randrange(0, len(loot))])
  return dungeonLoot
  
def generateEnemies():
  dungeonEnemies = []
  #enemy = sample(set(enemies.keys()), 5)
  #print(enemy)
  #enemy = enemies.get(enemy[0]).data
  #dungeonEnemies.append(enemy)
  for _ in range(0,4):
    enemy = enemies[randint(0, len(enemies)-1)]
    #print(enemy.name)
    dungeonEnemies.append(dumps(enemy.__dict__))
  #testDump("TEST", dungeonEnemies)
  return dungeonEnemies



class Dungeon:
  def __init__(self, name, number) -> None:
      self.name = name
      self.number = number
      self.passed = False
      self.gold = randrange(2, 100)
      self.loot = generateLoot()
      #self.items = generateItems()
      self.enemies = generateEnemies()
      self.data = {
        "name": self.name,
        "number": self.number,
        "passed": False,
        "gold": self.gold,
        "loot": self.loot,
        #"items": self.items
      }
  def passDungeon(self,player):
    print(f"Congrats! \nYou passed the dungeon and gained {self.gold} gold. \nGood luck in your next dungeon!")
    self.passed = True
    #player.inventory.append(self.loot)
    player.gold += self.gold
    
def generateDungeons(player):
  for dungeonNumber in range(0,15):
    dungeonType = types[randrange(len(types))]
    newDungeon = Dungeon(dungeonType, dungeonNumber)
    player.all_locations.append(dumps(newDungeon.__dict__))
  #newSave(player.name, player.all_locations)
  #print("Dungeons created")
  
class DictToClass(Dungeon):
  def __init__(self, data) -> None:
    self.name = data.get('name')
    self.number = data.get('number')
    self.passed = data.get('passed')
    self.gold = data.get('gold')
    self.loot = data.get('loot')
    #self.items = generateItems()
    self.enemies = data.get('enemies')
    self.data = data.get('data')
    
  def passDungeon(self, player):
    return super().passDungeon(player)