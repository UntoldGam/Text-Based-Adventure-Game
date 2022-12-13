from os.path import isfile 
from json import dump, loads
def newUser(data):
    # data = {"user": ..., "health": ...}
		file = open(f"./users/{data.userName}","w")
		file.write(dump(data))
		file.close() 
		return "User Created"

def saveUser(data):
	#if isfile(f"./users/{data['userName']}"):
	file = open(f"./users/{data['userName']}.json","r")
	content = loads(file.read())
	newData = {}
	for key in data:
		print(content, data[key])
		if data[key] != content[key]:
			print("different")
		newData.update({ f"{key}": data[key] })
		print(newData)
			# add to newData using the new data
	file.close()
	#file = open(f"./users/{data['userName']}.json","w")
	#file.close()
	#else:
	#	newUser(data)
