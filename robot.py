from weapon import Weapon
import random

class Robot: 
    def __init__(self, name):
        self.name = name
        self.health = random.randrange(25, 50, 1)   #random? w/in range 25-50?
        self.active_weapon = Weapon("saw-blade", "spinning swipe")


    def attack(self, dinosaur):
        print(f"{self.name} attacks!")
        robot_damage = random.randrange(2, 10, 1)
        dinosaur.health -= robot_damage
        print(f"{self.name} hits with {self.active_weapon.name} for {robot_damage} damage.")
        print(f"{dinosaur.name} has {dinosaur.health} health remaining.")
        return #or continue?        



# choose robot's weapon (ONLY after single one is working)

#create Fleet class??? choose 1 of 3 robots ... after this one is working.