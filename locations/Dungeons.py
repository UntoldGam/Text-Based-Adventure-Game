class Dungeon:
    def __init__(self, data):
        self.data = data
        self.name = data.Name
        self.func = open(f"../functions/{data.Name}.py", 'r').read()
