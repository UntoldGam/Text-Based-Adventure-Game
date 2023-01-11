from fileHandler import *
from init import *
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

username = None
while username == None:
    input_value = input("Please enter your username (max length is 8): ")
    if len(input_value) <= 8:
        username = input_value
        data = {"username": username, "health": 100, "passed_locations": []}
        newUser(data)
data = fetchUser(username)
if data != False:
    print(data)
    print(username)
    print("Please wait while the game loads/creates your game save.")
    init(username)
    