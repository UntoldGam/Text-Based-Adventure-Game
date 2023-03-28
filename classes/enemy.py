from random import randrange
class Enemy:
    def __init__(self, data) -> None:
      self.name = data.get('name')
      self.health = 100
      self.attack = randrange(5, 50)
      self.defense = randrange(5, 50)
      self.data = {
        "name": self.name,
        "health": self.health,
        "attack": self.attack,
        "defense": self.defense
      }