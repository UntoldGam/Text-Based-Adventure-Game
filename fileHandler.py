from os.path import isfile 
from json import dumps, loads

def validate(path):
	if isfile(path):
		return True
	else:
		return False

def openFile(filePath, method, fileContent): 
	try:
		if method:
			with open(filePath, method) as file:
				file.write(dumps(fileContent))
		elif not method:
			with open(filePath) as file:
				return loads(file.read())
	except:
		return print("Something went wrong")
		

def newSave(username, data):
	# adds a new file to dir /saves as {username}.json
	path = f"./saves/{username}.json"
	openFile(path) if validate(path) else openFile(path, "w", data)

def loadSave(username):
	# finds and reads a save file
	path = f"./saves/{username}.json"
	openFile(path) if validate(path) else print("No save found")

def fetchUser(username):
	path = f"./users/{username}.json"
	openFile(path) if validate(path) else openFile(path, "w", data)

def newUser(data):
	path = f"./users{data.get('username')}.json"
	method = "w"
	openFile(path, method, data)

def saveUser(data):
	path = f"./users{data.get('username')}.json"
	newData = {}
	openFile(path, "w", newData) if validate(path) else newUser(data)