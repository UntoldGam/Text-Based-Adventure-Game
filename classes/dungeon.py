class Dungeon:
    def __init__(self, data):
        print(data)
        print(data.get("name"))
        self.data = data
    def getData(self):
        print(self.data)
        return self.data