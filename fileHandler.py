from os.path import isfile 
from json import dumps, loads

def validate(path):
	if isfile(path):
		return True
	else:
		return False

def openFile(filePath, method, fileContent): 
	# method is only used when writing to a file using the "w" method
	# fileContent uses the same principle
	try:
		if method:
			# new method of opening - removes file.close() = does automatically
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