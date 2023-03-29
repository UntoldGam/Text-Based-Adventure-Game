from random import randrange, randint
from multipliers import decideDamage
class Enemy:
    def __init__(self, data) -> None:
      self.name = data.get('name')
      self.health = 100 or data.get('health')
      self.attack = randrange(5, 50)
      self.defense = randrange(5, 50) or data.get('defense')
      self.data = {
        "name": self.name,
        "health": self.health,
        "attack": self.attack,
        "defense": self.defense
      }
      
    def encounter(self, player):
      print(f"You have encounted a {self.name}")
      while self.health > 0:
          playerHitChance = randint(0, 4)
          enemyHitChance = randint(0, 4)
          personHit = None
          bonusApplied = False
          if playerHitChance > enemyHitChance:
              personHit = "enemy"
              bonusApplied = True
          elif enemyHitChance > playerHitChance:
              personHit = "player"
              bonusApplied = True
          else:
              if player.defense > self.defense:
                  personHit = "enemy"
              elif player.defense < self.defense:
                  personHit = "player"
              else:
                  persons = ["enemy", "player"]
                  personHit = persons[randint(
                      1, len(persons) + 1)]

          if bonusApplied:
            print("A bonus was applied!")
            hitChanceDecision = None
            if personHit == "enemy":
                hitChanceDecision = playerHitChance
            else:
                hitChanceDecision = enemyHitChance
            damage = decideDamage(
                player, self, hitChanceDecision / 10)
          else:
              damage = decideDamage(player, self)

          if personHit == "enemy":
              self.health -= damage
              self.health = round(self.health, 2)
              print(f"You hit the enemy for {round(damage,2)} hp ")
          else:
              player.decrement("health", damage)
              player.set("health", round(player.data.get("health"), 2))
              print(f"The enemy hit you for {round(damage,2)} hp")
          if self.health <= 0:
            return True
          elif player.data.get("health") <= 0:
            return False
          h=player.data.get("health")
          print(f"Health Stats \nEnemy: {self.health} \nPlayer: {h}")
          runAwayOrFight = input("Do you wish to \n1. Run away \n2. Stay and fight \n")
          while runAwayOrFight not in ["1","2"]:
            runAwayOrFight = input("Do you wish to \n1. Run away \n2. Stay and fight \n")
          if runAwayOrFight == "1":
            print("The enemy was too powerful for you")
            return False
          elif runAwayOrFight == "2":
            continue
class EnemyClass(Enemy):
  def __init__(self, data) -> None:
    self.name = data.get('name')
    self.health = data.get('health')
    self.attack = data.get('attack')
    self.defense = data.get('defense')
    self.data = data.get('data')
    
  def encounter(self, player):
   return super().encounter(player)