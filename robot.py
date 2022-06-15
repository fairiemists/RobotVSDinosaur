from weapon import Weapon
import random

class Robot: 
    def __init__(self, name):
        self.name = name
        self.health = random.randrange(25, 50, 1)   #random? w/in range 25-50?
        self.active_weapon = Weapon()

    def attack(self, dinosaur, weapon):
        print()
        print(f"{self.name} attacks!")
        robot_damage = random.randrange(2, 10, 1)
        dinosaur.health -= robot_damage
        # weapon.weapon_damage(dinosaur) ??? 
        # Add weapon_damage function in weapon file?
        print(f"{self.name} hits with {weapon.name} for {robot_damage} damage.")
        print(f"{dinosaur.name} has {dinosaur.health} health remaining.")
        print()
        # random number for damage w/in range (1-5?)
        return #or continue?        



# choose robot's weapon (ONLY after single one is working)

#create Fleet class??? choose 1 of 3 robots ... after this one is working.