# coding: utf-8
# license: GPLv3


class Attacker:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack
        try:
            if len(target._name)>0:
                f=open('hero.txt','w')
                f.write(str(target._health)+' '+str(target._attack)+' '+str(target._experience)+' '+target._name)
                f.close()
        except:pass
    def is_alive(self):
        return self._health > 0
