from weapon import Weapon
import random

class Robot: 
    def __init__(self, name):
        self.name = name
        self.health = random.randrange(25, 50, 1)   #random? w/in range 25-50?
        self.active_weapon = Weapon

    def attack(self, dinosaur, weapon):
        print(f"{self.name} attacks!")
        dinosaur.health -= weapon.attack_damage
        print(f"{self.name} hits for {weapon.attack_damage} damage.")
        # random number for damage w/in range (1-5?)
        return #or continue?        



# choose robot's weapon (ONLY after single one is working)

#create Fleet class??? choose 1 of 3 robots ... after this one is working.