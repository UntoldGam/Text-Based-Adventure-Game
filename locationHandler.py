# Used to generate all the dungeons for the game when a new game is made

from random import randrange

from fileHandler import *
from classes import dungeon
Dungeon = dungeon.Dungeon

dungeons = []
types = ["Ruin", "Cave", "Ravine"]
items = ["Dagger","Clock","Apple","Orange","Orangutan"]

class Dungeons():
    def __init__(self):
        dungeonNumber = 0
    
    def create():
        for _ in range(1,16): 
            for i in range(len(types)):
                print(types[i])
            dungeonType = types[randrange(1, len(types))]
            name = f"{dungeonType}_{dungeonNumber}"
            dungeonNumber += 1
            data = {"name": name, "rewards": {"Gold": 100, "Items": [items[randrange(1, len(items))]] } }
            # rewards = {"Gold": 100, "Items": ["Dagger", "Food"] }
            newDungeon = Dungeon(data)  
            dungeons.append(newDungeon.getData()) # a record of all dungeons, this is then added to the file

def init(username):
    
    #print(dungeons)
    newSave(username, dungeons)

def passDungeon(username, dungeon):
    userData = getData(username)
    
    passed_locations = userData["passed_locations"]
    passed_locations.append(dungeonClass)