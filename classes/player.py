class User:
    def __init__(self, data):
        self.name = data.get('username')
        self.health = data.get('health')
        self.passed_locations = []
    
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