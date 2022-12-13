from os.path import isfile 
from json import dumps, loads

def validateExistance(path):
	if isfile(path):
		return True
	else:
		return False
	

def newUser(data):
		file = open(f"./users/{data.get('userName')}.json","w")
		file.write(dumps(data))
		file.close() 
		return "User Created"

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
