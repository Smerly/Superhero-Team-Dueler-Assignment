from random import choice


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            self.heroes.remove(hero)
            foundHero = True
    if not foundHero:
        return 0

    def view_all_heroes(self):
        for hero in self.heroes.name:
            print[hero]


def stats(self):
    for hero in self.heroes:
        kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name, kd))


def revive_heroes(self, health=100):
    for hero in self.heroes:
        hero.current_health == hero.starting_health


def attack(self, other_team):
    ''' Battle each team against each other.'''

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
        living_heroes.append(hero)

    for hero in other_team.heroes:
        living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents) > 0:
        random_hero = choice(living_heroes)
        random_opponent = choice(living_opponents)

        random_hero.fight(random_opponent)

        if random_hero.is_alive == True:
            living_opponents.remove(random_opponent)
        else:
            living_heroes.remove(random_hero)
