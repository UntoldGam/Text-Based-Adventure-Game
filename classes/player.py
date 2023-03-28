class Player:
    def __init__(self, data) -> None:
        self.data = data
        self.name = data.get('username')
        self.health = data.get('health') or 100
        self.attack = data.get('attack') or 10
        self.defense = data.get('defense') or 10
        self.gold = data.get('gold') or 0
        self.inventory = data.get('inventory') or []
        self.all_locations = data.get('all_locations') or []
        self.passed_locations = data.get('passed_locations') or []
        self.lastCheckpoint = False # if True, restore health
    def set(self, property, newValue):
        self.data[property] = newValue
    
    def increment(self, property, change):
        self.data[property] += change
    def decrement(self, property, change):
        self.data[property] -= change
    
        