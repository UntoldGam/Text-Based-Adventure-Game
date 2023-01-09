from os.path import isfile 
from json import dumps, loads

def validate(path):
	if isfile(path):
		return True
	else:
		return False

def openFile(filePath, method, fileContent):
		if method:
			with open(filePath, method) as file:
				if method == "w":
					file.write(dumps(fileContent))
				elif method == "r":
					return loads(file.read())
	
def newSave(username, data):
	path = f"./saves/{username}.json"
	openFile(path) if validate(path) else openFile(path, "w", data)

def loadSave(username):
	path = f"./saves/{username}.json"
	message = ""
	openFile(path) if validate(path) else print("No save found")

def fetchUser(username):
	path = f"./users/{username}.json"
	openFile(path) if validate(path) else openFile(path, "w", data)

def newUser(data):
	path = f"./users{data['username']}.json"
	method = "w"
	openFile(path, method, data)

def saveUser(data):
	path = f"./users{data['username']}.json"
	if validate(path):
		newData = {}
		for key in data:
			newData.update({ f"{key}": data.get(key) })
		openFile(path, "w", newData)
	elif not validate(path):
		newUser(data)
