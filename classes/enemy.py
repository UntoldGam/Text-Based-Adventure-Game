class Enemy:
    def __init__(self, data):
        print(data)
        print(data.get("name"))
        self.data = data
        self.name = data.get('name')
        self.strength = data.get('strength')
        self.defense = data.get('defense')
        self.dungeon = data.get('current_dungeon')
        
    def getData(self):
        print(self.data)
        return self.data

    def complete(self):
        self.passed = True


