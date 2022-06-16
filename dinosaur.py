import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randrange(20, 30, 1)  
    
    def attack(self, robot):
        print(f"{self.name} attacks!")
        self.attack_power = random.randrange(2, 8, 1)
        dinosaur_damage = self.attack_power
        robot.health -= dinosaur_damage
        print(f"{self.name} hits for {self.attack_power} damage.")
        return 

    #create Herd class??? choose 1 of 3 dinosaurs ... after this one is working.