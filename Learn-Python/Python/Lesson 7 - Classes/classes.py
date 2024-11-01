# a basic class
# class TestClass:
#     test_var = "Hello"
#     another_var = "something"
#
#     def test_func(self):
#         print("Function in a class")
#         self.another_func("123")
#
#     def another_func(self, test_param):
#         print(test_param)
#
#
# # create an instance of the class
# test = TestClass()
# print(test.test_var)
# test.another_var = "a new value"
# print(test.another_var)
#
# # create another instance of the class
# test2 = TestClass()
# print(test2.another_var)
# test2.test_func()
# test2.another_func("Test")


# mage class
# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print("Magic is my superpower")
#         print(self.health, self.mana)
#
#     def attack(self, target):
#         target.health -= 10


# class Monster:
#     health = 40


# mage = Mage(100, 200)
# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)


# inheritance


class Human:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("attack")


class Warrior(Human):
    def __init__(self, health, defense):
        super().__init__(health)
        self.defense = defense


class Barbarian(Human):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage = damage


warrior = Warrior(50, 5.5)
barbarian = Barbarian(100, 8.1)
warrior.attack()
barbarian.attack()
print(warrior.health)
