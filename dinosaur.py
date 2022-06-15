import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randrange(25, 50, 1)  #random? w/in range
    
    def attack(self, robot):
        print()
        print(f"{self.name} attacks!")
        self.attack_power = random.randrange(2, 10, 1)
        dinosaur_damage = self.attack_power
        robot.health -= dinosaur_damage
        print(f"{self.name} hits for {self.attack_power} damage.")
        print(f"{robot.name} has {robot.health} health remaining.")
        print()
        # random number for damage w/in range (1-5?)
        return #or continue?

    #create Herd class??? choose 1 of 3 dinosaurs ... after this one is working.