from random import randrange, randint, sample
from fileHandler import saveUser, testDump, testDump3
from .enemy import Enemy
from json import dumps, loads
types = ["Ruin", "Cave", "Ravine", "Bandit Camp"]
items = ["Dagger", "Clock", "Apple", "Orange"]
enemies = [
    Enemy({ "name": "Goblin"}),
    Enemy({"name": "Bandit"}), 
    Enemy({"name": "Spider"}),
    Enemy({ "name": "Ghost"}),
    Enemy({ "name": "Troll", "attack": 49 , "defense": 25,"health": 250 }),
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
    player.increment("gold", self.gold)
    
  def encounterItem(self, player):
      items = self.loot
      item = items[randint(0, len(items)-1)]
      
      item_boost, item_stat = item.get('id').split('_')[0], item.get('id').split('_')[1]
      item_boost, item_stat = int(item_boost), str(item_stat)
      print(item_boost, item_stat) 
      choice = input(f"You come across a {item.get('name')} \n You can either: \n1. Pick it up and inspect it(use it) \n2. Ignore it and choose the other path")
      while choice not in ["1","2"]:
        choice = input(f"You come across a {item.get('name')} \n You can either: \n1. Pick it up \n2. Ignore it and choose the other path")
      if choice in ["1", "2"]:
          if choice == "1":
              print("You pickup the item and feel a strange feeling in your stomach")
              print(type(player))
              value = player.data.get(item_stat)
              player.increment(item_stat, value)
              print(f"Your {item_stat} stat was just doubled, it's now {value}")
              storeItem=input("There's still some boost left, would you like to store this for later? y = yes, n = no")
              while storeItem not in ["y", "n"]:
                storeItem=input("There's still some boost left, would you like to store this for later? y = yes, n = no")
              if storeItem == "y":
                player.data.get("inventory").append(item.get('id'))
                saveUser(player.data)
              print(f"You exit the {self.name} and move onto the next")
              return 1
          elif choice == "2":
              print(f"You go through the opposite tunnel in the {self.name}")
              return 2
def generateDungeons(player):
  for dungeonNumber in range(0,15):
    dungeonType = types[randrange(len(types))]
    newDungeon = Dungeon(dungeonType, dungeonNumber)
    player.data.get("all_locations").append({f"{newDungeon.name}_{newDungeon.number}": dumps(newDungeon.__dict__)})
    #testDump3("",player.all_locations)
  #newSave(player.name, player.all_locations)
  #print("Dungeons created")
  
class DungeonClass(Dungeon):
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
  def encounterItem(self, player):
    return super().encounterItem(player)