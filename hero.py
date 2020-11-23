from random import choice

from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        fighters = [self, opponent]
        winner = (choice(fighters))

        return print(f'{winner.name} is the winner!')

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            total_block = armor.block()
        return total_block

    def take_damage(self, damage):
        health_lost = damage - self.defend(0)
        self.current_health -= health_lost
        return self.current_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_potato_throw(self, potato_throw):
        self.abilities.append(potato_throw)

    def add_armor(self, armor):
        self.armors.append(armor)


#

# # Testing ahead # # # # Testing ahead # # # # Testing ahead # # # # Testing ahead # # # # Testing ahead # # # # Testing ahead # # # # Testing ahead # # # #

#


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")

#     hero1.fight(hero2)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)

#     hero.add_ability(ability)

#     print(hero.abilities)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     potato_throw = Ability('potato_Throw', 100000)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_potato_throw(potato_throw)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
