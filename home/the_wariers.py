"""
The Warriors

I'm sure that many of you have some experience with computer games.
But have you ever wanted to change the game so that the characters or a game world
would be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it)
you’ll have a chance "to sit in the developer's chair" and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel.
You need to create the class Warrior, the instances of which will have 2 parameters -
health (equal to 50 points) and attack (equal to 5 points),
and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case).
In addition you have to create the second unit type - Knight,
which should be the subclass of the Warrior but have the increased attack - 7.
Also you have to create a function fight(),
which will initiate the duel between 2 warriors and define the strongest of them.
The duel occurs according to the following principle:
every turn one of the warriors will hit another one
and the last will lose his health in the same value as the attack of the first warrior.
After that, the second warrior will do the same to the first one.
If in the end of the turn the first warrior has > 0 health and the other one doesn’t,
the function should return True, in the other case it should return False.

Input: The warriors.
Output: The result of the duel (True or False).
Precondition: 2 types of units
"""

from dataclasses import dataclass
from itertools import cycle, permutations
from typing import Union


@dataclass
class Warrior:
    health: int = 50
    attack: int = 5

    @property
    def is_alive(self):
        return self.health > 0


@dataclass
class Knight(Warrior):
    attack: int = 7


def fight(unit_1: Union[Warrior, Knight], unit_2: Union[Warrior, Knight]) -> bool:

    for x, y in cycle(permutations((unit_1, unit_2))):
        if x.is_alive and y.is_alive:
            y.health -= x.attack
        else:
            break

    return unit_1.is_alive


if __name__ == "__main__":

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
