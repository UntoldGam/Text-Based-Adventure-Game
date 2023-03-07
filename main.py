from fileHandler import *
from locationHandler import *
from classes.player import Player

from sys import stdout
from time import sleep
from sshkeyboard import listen_keyboard
from tabulate import tabulate
# have an init function that makes all the ruins:
# Populate a python variable (dictionary) with locations AFTER they've gone through the Class Construction
# Basically:
"""
The program will use a random algorithm to choose a random set of rewards and then put the data chosen through the corresponding 
class e.g. Dungeon (it'll use a list of specific dungeon types to assign each dungeon a type EXCEPT the final dungeon as it is a 
set type)
"""

#data = { "userName": "example", "health": 120, "h_multiplier": 0.2, "passed_locations": ['ruin1','ruin2','ruin3'] }
#saveUser(data)

# the above code is a test for saving data, ignore it

# doesn't include any validation of length just yet, possibly a 5 - 8 maximum due to it being the name of a file 
#  or we can simplify it into one JSON file or something rather than multiple

def typewrite(words):
    for char in words:
        sleep(0.03)
        stdout.write(char)
        stdout.flush()
typewrite("Welcome to [Game Name]! a text-based adventure game...")    
print("\n\n-------------------------------------------------------------------\n")
typewrite("Here you will encounter Challenges, face puzzles and make crucial decisions all of which alter the course of the game and the overall outcome of your Journey...\nDisplayed in the top right corner you will see your Health Points, and Timer, these affect your score at the end of the game...\nListed below includes the controls for the game, you will need to use these and can always refer back to them at any point by pressing [C]...\nAt the end of each level, you will pass a checkpoint this saves your progress, lose all your health and you will go back to your most recent checkpoint so choose wisely...")
print("\n-------------------------------------------------------------------\n\n")
tabledata=([["Control","Key"],["Start","SPACE"],["HINT","?"],["Controls","C"],["Pause","P"],["Veiw Clues","#"],["Veiw Health Points","H"],["Veiw Time","T"]])
print(tabulate(tabledata,headers="firstrow", tablefmt="rounded_grid"))

if __name__ == "__main__":
    username = None
    while username == None:
        input_value = input("Please enter your username (max length is 8): ")
        if len(input_value) <= 8:
            username = input_value
            data = {"username": username, "health": 100, "passed_locations": []}
            newUser(data)
    data = fetchUser(username)
    player=Player(data)
    if data != False:
        print(data)
        print(username)
        print("Please wait while the game finds your game save.")
        initLocations(player)