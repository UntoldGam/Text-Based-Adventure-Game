# Used to generate all the dungeons for the game when a new game is made

from random import randrange

from fileHandler import newSave, getData
from .classes.dungeon import Dungeon

dungeons = []
types = ["Ruin", "Cave", "Ravine"]
items = ["Dagger","Clock","Apple","Orange","Orangutan"]

def createDungeons():
    dungeonNumber = 0
    for _ in range(1,16): 
        for i in range(len(types)):
            print(types[i])
        dungeonType = types[randrange(1, len(types))]
        name = f"{dungeonType}_{dungeonNumber}"
        dungeonNumber += 1
        data = {"name": name, "loot": {"Gold": 100, "Items": [items[randrange(1, len(items))]] } }
        # rewards = {"Gold": 100, "Items": ["Dagger", "Food"] }
        newDungeon = Dungeon(data)  
        dungeons.append(newDungeon.getData()) # a record of all dungeons, this is then added to the file

def LocationCreation(player):
    #print(dungeons)
    if player.dungeons == []:
        createDungeons()
        if dungeons == []:
            print("Error: no dungeons")
        else:
            player.update("dungeons",dungeons)

def passDungeon(player, dungeon):
    userData = getData(player.name)
    
    passed_locations = userData["passed_locations"]
    passed_locations.append(dungeonClass)