# Used to generate all the dungeons for the game when a new game is made

from json import dumps, loads
from os.path import isfile
from random import randrange

from classes import dungeon
Dungeon = dungeon.Dungeon
from fileHandler import *

# Makes a save file which will hold the dungeons
dungeons = []
types = ["Ruin", "Cave", "Ravine"]
items = ["Dagger","Clock","Apple","Orange","Orangutan"]
def init(username):
    dungeonNumber = 0
    for _ in range(1,16): 
        for i in range(len(types)):
            print(types[i])
        dungeonType = types[randrange(1, len(types))]
        name = f"{dungeonType}_{dungeonNumber}"
        dungeonNumber = dungeonNumber + 1
        data = {"name": name, "rewards": {"Gold": 100, "Items": [items[randrange(1, len(items))]] } }
        # rewards = {"Gold": 100, "Items": ["Dagger", "Food"] }
        newDungeon = Dungeon(data)  
        dungeons.append(newDungeon.getData()) # a record of all dungeons, this is then added to the file
        
    
    save_name = f"{username}"
    print(dungeons)
    newSave(save_name, dungeons)