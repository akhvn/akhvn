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
