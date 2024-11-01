# Create a Monster class where you can set a health and damage attribute on creation.
# It should also inherit from an entity class to get an attack method (that prints "attack" & the damage amount)
# When an instance of the class is printed it returns "a monster with {health}hp"


class Entity:
    def attack(self):
        print(f"attack with {self.damage} damage")


class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f"a monster with {self.health} hp"


monster = Monster(100, 10)
print(monster.health)
monster.attack()
print(monster)
