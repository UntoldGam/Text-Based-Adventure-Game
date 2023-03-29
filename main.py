from fileHandler import *
from classes.player import Player, PlayerClass
from classes.enemy import EnemyClass
from classes.dungeon import generateDungeons, DungeonClass
from multipliers import decideDamage

from os import system, name
from sys import exit
from json import loads
from sys import stdout
from time import sleep
# from sshkeyboard import listen_keyboard
from tabulate import tabulate
from random import randint, randrange

# data = { "userName": "example", "health": 120, "h_multiplier": 0.2, "passed_locations": ['ruin1','ruin2','ruin3'] }
# saveUser(data)

# the above code is a test for saving data, ignore it

# doesn't include any validation of length just yet, possibly a 5 - 8 maximum due to it being the name of a file
#  or we can simplify it into one JSON file or something rather than multiple
DEBUG = True

def clear():
    system('cls' if name == 'nt' else 'clear')

def typewrite(words):
    if DEBUG:
        print(words)
    else:
        for char in words:
            sleep(0.03)
            stdout.write(char)
            stdout.flush()


typewrite("Welcome to the text-based adventure game...")
print("\n\n-------------------------------------------------------------------\n")
# typewrite("Here you will encounter Challenges, face puzzles and make crucial decisions all of which alter the course of the game and the overall outcome of your Journey...\nAt the end of each level, you will pass a checkpoint this saves your progress, lose all your health and you will go back to your most recent checkpoint so choose wisely...")
typewrite("Here you will encounter countless dungeons all of which contain enemies.\nAt the end of each dungeon, you will have two choices: \n1. Save your progress and replenish any health \n2. Continue (and risk losing your progress)\nLose all your health and you will go back to a checkpoint and your health will be restored, choose wisely...")
print("\n-------------------------------------------------------------------\n\n")
# tabledata=([["Control","Key"],["Start","SPACE"],["HINT","?"],["Controls","C"],["Pause","P"],["Veiw Clues","#"],["Veiw Health Points","H"],["Veiw Time","T"]])
# print(tabulate(tabledata,headers="firstrow", tablefmt="rounded_grid"))  
             
def enemies(player, dungeon, raw_dungeon):
    for enemy in dungeon.enemies:
        enemy = loads(enemy)
        enemy = EnemyClass(enemy)
        openInv = input("Would you like to view your inventory? Yes (y) or No (n) \n")
        if openInv == "y":
            if player.inventory == []:
                print("Your inventory is empty")
                enemies(player, dungeon, raw_dungeon)
            else:
                print(f"Your inventory: \n");
                tableData =[[item for item in player.inventory]]
                print(tabulate(tableData, headers="firstrow", tablefmt="rounded_grid"))
                useItem=input("Would you like to use an item from your inventory? (y = yes, n = no) ")
                if useItem == "y":
                    item=input("What item would you like to use? ")
                    item = dungeon.data.get("loot")[item]
                    print(type(item))
                    print(type(loads(item)))
                    item_boost, item_stat = int(item.get('id').split('_')[0]), str(item.get('id').split('_')[1])
                    print(item_boost, item_stat)
                    value = player.get(item_stat)
                    player.increment(item_stat, value)
                    print(f"Your {item_stat} stat was just increased by x{item_boost}, it's now {player[item_stat]}") 
        choice = input("Do you want to go left [l] or right [r]? \n")
        while choice not in ["l", "r"]:
            choice = input("Do you want to go left [l] or right [r]? \n")
        if choice in ["l","r"]:
            enemyFaced = False
            if choice == "l": 
                enemyDefeated = enemy.encounter(player)
                enemyFaced = True
            elif choice == "r":
                item = dungeon.encounterItem(player)
                if item in [1, 2]:
                    if item == 1:
                        continue
                    elif item == 2:
                        enemyDefeated = enemy.encounter(player)
                        enemyFaced = True
            if enemyFaced and enemyDefeated:
                if player.data.get('health') > 0:
                    print(f"{enemy.name} defeated!")
                    player.increment("gold", randint(1, 50))
                elif player.data.get('health') <= 0:
                    if player.lastCheckpoint != False:
                        player.set("health", 100)
                        player.set("lastCheckpoint", False)
                        continue
                    else:
                        gameOver(player)
            elif player.data.get('health') <= 0:
                if player.lastCheckpoint != False:
                    player.set("health", 100)
                    player.set("lastCheckpoint", False)
                else:
                    gameOver(player)
    print(f"All enemies have been defeated for the {dungeon.name} {dungeon.number}: dungeon passed.")
    player.data.all_locations.remove(raw_dungeon)
    player.data.passed_locations.append(dungeon.data)
    dungeon.passDungeon(player)
    checkpointDecision = input("Do you wish to go to a checkpoint and use a health potion (1) or go to the next dungeon? ")
    if checkpointDecision in ["1", "2"]:
        if checkpointDecision == "1": # only really done if you want to 
            player.set("lastCheckpoint", True) # if you die to an enemy in the next dungeon, you'll go to the next enemy
            player.set("health", 100)
            print("Your health was replenished by a health potion at the checkpoint")
            saveUser(player.data)


def gameOver(player):
    print("GAME OVER\n")
    n=player.data.get("name")
    print(f"You died, {n}. You now have the option to either exit or play again.\n")
    option = input("Options: \n1. Play Again \n2. Exit  \n")
    if option in ["1","2"]:
        if option == "1":
            deleteUser(player.data.get("name"))
            play_game()
        else:
            print("Thank you for playing!")
            exit()
def play_game():
    username = None
    while username == None:
        input_value = input("Please enter your username (max length is 8): ")
        if len(input_value) <= 8:
            username = input_value
    
    data = newUser(username) 
    # if the user exists, the above will fetch the users data
    # if the user doesn't exist, the above will create and return the users data
    if data != False:
        player = Player(data)
        #print(data)
        #print(username)
        #print("Please wait while the game finds your game save.")
        generateDungeons(player)
        for dungeon in player.data.get("all_locations"):
            #print(dungeon)
            raw_dungeon = dungeon
            dungeon = loads(dumps(dungeon))
            
            dungeon_dict = dungeon
            #print(dungeon_dict)
            dungeon_name = list(dungeon_dict)[0]
            print(dungeon_name)
            dungeon = loads(dungeon_dict.get(dungeon_name))
            dungeon = DungeonClass(dungeon)
            if player.lastCheckpoint != False:
                player.lastCheckpoint = dungeon.name
            else:
                player.lastCheckpoint = False

            words=["old", "mysterious", "creepy"]
            print(f"You enter a {words[randrange(0,len(words)-1)]} {dungeon.name}")
    
            enemies(player, dungeon, raw_dungeon)
                
        if (player.data.get("passed_locations") == player.data.get("all_locations")) and player.data.get("passed_locations") != [] and player.data.get("all_locations") != []:
            risk = input("Congratulations, you have beaten all dungeons. You now have the chance to \n1. Double your gold OR lose half your gold \n2. Not risk it and end the game")
            while risk not in ["1", "2"]:
                if risk == "1":
                    chance = randint(0,10)
                    if chance >= 5:
                        print("Congrats, your gold has been doubled")
                        player.gold *= 2
                        print(f"Your gold is now {player.gold}")
                    elif chance < 5:
                        print("You lost half your gold.")
                        player.gold -= (player.gold / 2) # half your gold is now gold
                        print(f"Your gold is now {player.gold}")
                elif risk == "2":
                    gameOver()
        else:
            print("There was an error when your dungeons were added to the passed_locations property of your player: play the game again.")

play_game()        