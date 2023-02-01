from .character import Character

class Enemy(Character):
    def __init__(self, data):
        print(data)
        print(data.get("name"))
        self.data = data # array
        self.name = data.get('name') # string
        self.strength = data.get('strength') # float
        self.defense = data.get('defense') # float
        self.dungeon =  data.get('current_dungeon') # Class


