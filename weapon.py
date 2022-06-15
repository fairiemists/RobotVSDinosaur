import random

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def attack_damage(self):
        self.attack_power = random.randrange(2, 10, 1)
        return
    
    #choose one of three? ...after this one is working.