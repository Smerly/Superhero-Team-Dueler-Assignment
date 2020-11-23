from random import choice


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        fighters = [self, opponent]
        winner = (choice(fighters))

        return print(f'{winner.name} is the winner!')


if __name__ == '__main__':
    my_hero = Hero('Grace Hopper', 200)
    print(my_hero.name)
    print(my_hero.current_health)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
