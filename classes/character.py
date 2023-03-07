class Character:
    def __init__(self, data):
            super().__init__(self, data)
            self.name = data.get('username')
            self.health = data.get('health') or 100 # default health
            self.score = data.get('score') or 0 # default score
            self.attack = data.get('attack') or 10
            self.defense = data.get('defense') or 0.1
            self.dungeons = data.get('dungeons') or []
            self.passed_locations = data.get('passed_locations') or [] # default passed locations
            self.inventory = data.get('inventory') or [] # default inventory
            self.currentDungeon = False

    def get(self, property):
        return self[property]

    def set(self, property, newValue):
        try:
            self[property] = newValue
            if self[property] == newValue: print(f"Set {property} to {newValue}")
        except:
            return print(f"Couldn't set {property} to {newValue}")
        
            
    def update(self, property, change, operation):
        errorMessage=f"Couldn't update {property} by {change} using {operation}."
        try:
            if operation == "add":
                self[property] += change
            elif operation == "subtract":
                self[property] -= change
            else:
                print(errorMessage)
        except:
            print(errorMessage)