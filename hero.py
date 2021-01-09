# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.
"""

class Wizard(Attacker):
    _lvl = 1
    def __init__(self):
        self._health = 75
        self._attack = 125
        self._experience = 0
        self._name = name
        self._inportance = 1.5
class Healer(Attacker):
    _lvl = 1
    def __init__(self):
        self._health = 50
        self._attack = 50
        self._experience = 0
        self._name = name
        self._inportance = 0.5
class Jagernaut(Attacker):
    _lvl = 1
    def __init__(self):
        self._health = 125
        self._attack = 60
        self._experience = 0
        self._name = name
        self._inportance = 1.15
class Imba(Attacker):
    _lvl = 1
    def __init__(self):
        self._health = 1000
        self._attack = 1000
        self._experience = 0
        self._name = name
        self._inportance = 5


def attack(self, target):
    target._health -= self._attack
