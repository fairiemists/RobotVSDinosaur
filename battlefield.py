from dinosaur import Dinosaur
from robot import Robot

import random #??

class Battlefield:
    def __init__(self, name):
        self.name = name
        self.robot = Robot("Megatron")
        self.dinosaur = Dinosaur("T-rex", "tailsweep")
        self.winner = ""



      

    def display_welcome(self, robot, dinosaur):
        print(f"{robot.name} thunks into the {self.name}. Its {self.robot.active_weapon.name} at the ready. ")
        print(f"{dinosaur.name} stomps into the {self.name}. Its tail lashing threateningly.")

        print(f"Welcome to the epic battle of ROBOT vs DINOSAUR!!!")
        print(f"Today we have {robot.name} and {dinosaur.name}.")
        print(f"Ready...Set...FIGHT!")
        #self.battle_phase(self.robot, self.dinosaur)
        return 



    def display_winner(self, winner):
        print(f"{winner.name} executes a critical blow. {winner.name} WINS!!")
        print(f"{self.name} is safe once more.")



    def battle_phase(self, robot, dinosaur):
        
        result = random.choice(robot, dinosaur)
        if (result == robot):
            self.robot.attack(dinosaur)
        else:
            self.dinosaur.attack(robot)


        self.dinosaur.attack(robot)
        while (self.robot.health > 0):
            print(f"{self.robot.name} is still standing!") 
            print()
            self.battle_phase(self.robot, self.dinosaur) 
            break
        while (self.robot.health <= 0):
            winner = self.dinosaur
            self.display_winner(winner)
            return
            
        self.robot.attack(dinosaur)
        while (self.dinosaur.health > 0): 
            print(f"{self.dinosaur.name} is still standing!") 
            print()
            self.battle_phase(self.robot, self.dinosaur) 
            break
        while (self.dinosaur.health <= 0):
            winner = self.robot
            self.display_winner(winner)
            return            

    def run_game(self):
        print()
        self.display_welcome(self.robot, self.dinosaur)
        print()
        self.battle_phase(self.robot, self.dinosaur)
        #print()
        #self.display_winner(self.winner)
        
        




