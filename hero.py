from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    # This takes in two heros and makes them fight until one dies. If neither can kill each other, it makes it a draw
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print('Draw')
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                true_damage_against_opponent = self.attack() - opponent.defend()
                self.take_damage(true_damage_against_opponent)

                true_damage_against_self = opponent.attack() - self.defend()
                opponent.take_damage(true_damage_against_self)

            if self.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f'{opponent.name} has won the battle!')
            elif opponent.is_alive():
                opponent.add_kill(1)
                self.add_death(1)
                print(f'{self.name} has won the battle!')

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num.deaths

    # This takes the ability from the object and turns it into raw damage
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    # This takes the armor value from the object and turns it into how much damage is blocked
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    # This takes raw damage and turns it into true damage
    def take_damage(self, damage):
        health_lost = damage - self.defend()
        self.current_health -= health_lost
        return self.current_health

    # Type of ability
    def add_ability(self, ability):
        self.abilities.append(ability)

    # Type of ability
    def add_potato_throw(self, potato_throw):
        self.abilities.append(potato_throw)

    # Type of armor
    def add_armor(self, armor):
        self.armors.append(armor)

    # Checks if someone is dead
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True


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

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
