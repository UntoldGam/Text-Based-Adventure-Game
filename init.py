# Used to generate all the dungeons for the game when a new game is made

from os.path import isfile 
from json import dumps, loads
from fileHandler import *
from classes import dungeon
from random import randrange

# Makes a save file which will hold the dungeons
dungeons = {}
dungeonNumber = 1
types = ["Ruin", "Cave", "Ravine"]

def init(username):
    for _ in range(1,16): 
        for i in range(len(types)):
            print(types[i])
        dungeonType = types[randrange(1, len(types))]
        name = f"{dungeonType}_{dungeonNumber}"
        dungeonNumber += 1
        data = {"name": name, "rewards": {"Gold": 100, "Items": [] } }
        # rewards = {"Gold": 100, "Items": ["Dagger", "Food"] }
        dungeons.update(dungeon(data)) # a record of all dungeons, this is then added to the file
        
    
    save_name = f"{username}"
    newSave(save_name, dungeons)