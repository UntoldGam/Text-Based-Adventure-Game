from os.path import isfile 
from json import dumps, loads

def validate(path):
	if isfile(path):
		return True
	else:
		return False

def openFile(filePath, method, fileContent):
	if validate(path):
		if method:
			with open(filePath, method) as file:
				action = "write" if method == "w" else "read"
				if method == "w":
					file.write(dumps(fileContent))
				elif method == "r":
					return loads(file.read())
			
def newSave(username, data):
	path = f"./saves/{username}.json"
	if validate(path):
		openFile(path)
	if not validate(f"./saves/{name}.json"):
		openFile(f"./saves/{name}.json", "w", data)

def loadSave(username):
	path = f"./saves/{username}.json"
	if validate(path):
		openFile(path)


	if isfile(f"./saves/{username}.json"):
		file = open(f"./saves/{username}.json")
		content = loads(file.read())
		file.close()
		return content	
	else:
		return False


	
def fetchUser(username):
	if isfile(f"./users/{username}.json"):
		with open(f"./users/{username}.json", "r") as file:
			content = loads(file.read())
			return content
	else:
		return False

def newUser(data):
		file = open(f"./users/{data.get('userName')}.json","w")
		file.write(dumps(data))
		file.close() 
		return True

def saveUser(data):
	if isfile(f"./users/{data.get('userName')}.json"):
		file = open(f"./users/{data.get('userName')}.json","r")
		content = loads(file.read())
		newData = {}
		for key in data:
			#print(content, data.get(key))
			newData.update({ f"{key}": data.get(key) })
			#print(newData)
		file = open(f"./users/{data.get('userName')}.json","w")
		file.write(dumps(newData))
		file.close()
	else:
		newUser(data)
