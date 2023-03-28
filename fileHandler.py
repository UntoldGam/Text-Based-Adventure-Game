from os import remove
from os.path import isfile
from json import dumps, loads

def validate(path):
	if isfile(path):
		return True
	else:
		return False

def readFile(filePath): 
	try:
		with open(filePath) as file:
			return loads(file.read())
	except:
		return print("Something went wrong")
		
def writeFile(filePath, method, fileContent):
	try:
		if method:
			with open(filePath, method) as file:
				file.write(dumps(fileContent))
				return True
		else:
			return False
	except:
		return print("Something went wrong")
	
def newSave(username, data):
	path = f"./saves/{username}.json"
	readFile(path) if validate(path) else writeFile(path, "w", data)

def loadSave(username):
	# finds and reads a save file
	path = f"./saves/{username}.json"
	readFile(path) if validate(path) else print("No save found")

def testDump(name, data):
  path=f"{name}.json"
  if validate(path):
    remove(path)
  with open(path, "w") as file:
    file.write(dumps(data))

def newUser(username=None):
	if username == None:
		return False 
	else:
		path = f"./users/{username}.json"
		data = { "username": username, "health": 100, "attack": 10, "defense": 10, "gold": 0, "inventory": [], "passed_locations": [], "all_locations": [] }
		method = "w"
		writeFile(path, method, data)

def fetchUser(username):
	path = f"./users/{username}.json"
	return readFile(path) if validate(path) else print("No user found")

def saveUser(data):
	path = f"./users/{data.get('username')}.json"
	writeFile(path, "w", data) if validate(path) else newUser(data)