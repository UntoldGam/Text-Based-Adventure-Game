from fileHandler import *
from locationHandler import *
from classes.player import Player
from classes.dungeon import generateDungeons, DictToClass
from multipliers import decideDamage

from json import loads
from sys import stdout
from time import sleep
# from sshkeyboard import listen_keyboard
from tabulate import tabulate
from random import randint

# data = { "userName": "example", "health": 120, "h_multiplier": 0.2, "passed_locations": ['ruin1','ruin2','ruin3'] }
# saveUser(data)

# the above code is a test for saving data, ignore it

# doesn't include any validation of length just yet, possibly a 5 - 8 maximum due to it being the name of a file
#  or we can simplify it into one JSON file or something rather than multiple
DEBUG = True


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


def encounterEnemy(player, enemy):
    print(f"You have encounted a {enemy.get('name')}")
    while enemy.get('health') > 0:
        playerHitChance = randint(0, 4)
        enemyHitChance = randint(0, 4)
        personHit = None
        bonusApplied = False
        if playerHitChance > enemyHitChance:
            personHit = "enemy"
            bonusApplied = True
        elif enemyHitChance > playerHitChance:
            personHit = "player"
            bonusApplied = True
        else:
            if player.defense > enemy.get('defense'):
                personHit = "enemy"
            elif player.defense < enemy.get('defense'):
                personHit = "player"
            else:
                persons = ["enemy", "player"]
                personHit = persons[randint(
                    1, len(persons) + 1)]

        if bonusApplied:
            hitChanceDecision = None
            if personHit == "enemy":
                hitChanceDecision = playerHitChance
            else:
                hitChanceDecision = enemyHitChance
            damage = decideDamage(
                player, enemy, hitChanceDecision / 10)
        else:
            damage = decideDamage(player, enemy)

        if personHit == "enemy":
            enemy.health -= damage
            print(f"You hit the enemy for {damage} hp")
        else:
            player.health -= damage
            print(f"The enemy hit you for {damage} hp")
             

def encounterItem(player, dungeon):
    items = dungeon.loot
    item = items[randint(0, len(items)-1)]
    item_boost, item_stat = int(item.get('id').split('_')[0]), str(item.get('id').split('_')[1])
    print(item_boost, item_stat) 
    choice = input(f"You come across a {item.get('name')} \n You can either: \n1. Pick it up and inspect it(use it) \n2. Ignore it and choose the other path")
    if choice in ["1", "2"]:
        if choice == "1":
            print("You pickup the item and feel a strange feeling in your stomach")
            print(type(player))
            value = player.data.get(item_stat)
            player.increment(item_stat, value)
            print(f"Your {item_stat} stat was just doubled, it's now {value}")
            print(f"You exit the {dungeon.name} and move onto the next")
            return 1
        elif choice == "2":
            print(f"You go through the opposite tunnel in the {dungeon.name}")
            return 2
def gameOver(player):
    print("GAME OVER\n")
    print(f"You died a warrior's death {player.name}\n")
    option = input("Options: \n1. Play Again \n2. Exit")

def play_game():
    username = None
    while username == None:
        input_value = input("Please enter your username (max length is 8): ")
        if len(input_value) <= 8:
            username = input_value
            newUser(username)
    data = fetchUser(username)
    if data != False:
        player = Player(data)
        #print(data)
        #print(username)
        #print("Please wait while the game finds your game save.")
        generateDungeons(player)
        for dungeon in player.all_locations:
            dungeon = loads(dungeon)
            dungeonClass = DictToClass(dungeon)
            #print(type(dungeon))
            #print(dungeon)
            words=["old", "mysterious", "creepy"]
            print(f"You enter a {words[randrange(0,len(words)-1)]} {dungeonClass.name}")
            openInv = input("Would you like to view your inventory? Yes (y) or No (n) ")
            if openInv == "y":
                print(f"Your inventory: \n")
                tableData =[[item for item in player.inventory]]
                print(tabulate(tableData, headers="firstrow", tablefmt="rounded_grid"))
            for enemy in dungeon.get('enemies'):
                enemy = loads(enemy)
                choice = input("Do you want to go left [l] or right [r] or exit [e]?")
                if choice in ["l","r","e"]:
                    enemyFaced = False
                    if choice == "l": 
                        encounterEnemy(player, enemy)
                        enemyFaced = True
                    elif choice == "r":
                        item = encounterItem(player, dungeon)
                        if item == 1:
                            continue
                        elif item == 2:
                            encounterEnemy(player, enemy)
                            enemyFaced = True
                    if enemyFaced:
                        if player.health > 0:
                            print(f"{enemy.get('name')} defeated!")
                            player.increment("gold", randint(1, 50))
                        elif player.health == 0:
                            if player.lastCheckpoint:
                                player.health = 100
                                continue
                            else:
                                gameOver()
            print(f"All enemies have been defeated for the {dungeonClass.name} {dungeon.get('number')}: dungeon passed.")
            player.passed_locations.append(dungeon.get('data'))
            dungeon.passDungeon(player)
            checkpointDecision = input("Do you wish to go to a checkpoint and use a health potion (1) or go to the next dungeon? ")
            if checkpointDecision in ["1", "2"]:
                if checkpointDecision == "1": # only really done if you want to 
                    player.lastCheckpoint = True # if you die to an enemy in the next dungeon, you'll go to the next enemy
                    player.health = 100
                    print("Your health was replenished by a health potion at the checkpoint")
                    saveUser(player.data)
        if player.passed_locations == player.all_locations:
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