# coding: utf-8
# license: GPLv3


class Attacker:
    _health = None
    _attack = None
    _experience = None
    _lvl = 0
    
    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0
    
    def add_experience(self):
        self._experience = self._experience + 25
        if self._experience >= 0 and self._experience <= 99:
            self._lvl = 1
        elif self._experience >= 100 and self._experience <= 199:
            self._lvl = 2
        elif self._experience >= 200 and self._experience < 299:
            self._lvl = 3
        elif self._experience >= 300 and self._experience <= 399:
            self._lvl = 4
        elif self._experience >= 400 and self._experience <= 500:
            self._lvl = 5
