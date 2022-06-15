from dinosaur import Dinosaur
from robot import Robot

import random #??

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    
    def run_game(self):
        print()
        #call display_welcome
        self.display_welcome
        print()
        #call battle_phase & loop until zero or lower
        self.battle_phase
        print()
        #call display_winner
        self.display_winner
        

    def display_welcome(self, robot, dinosaur):
        #witty welcome (hype it up!)
        print(f"Welcome to the epic battle of ROBOT vs DINOSAUR!!!")
        print(f"Today we have {robot} and {dinosaur}.")
        print(f"Ready...Set...FIGHT!")
        self.battle_phase()
        return #or continue?

    def battle_phase(self, robot, dinosaur, winner):
        #loop until at zero or lower
        #attack = random.choice(robot, dinosaur) ??
        dinosaur.attack(robot)
        while (robot.health >= 1):
            continue 
        else:
            winner == dinosaur
            self.display_winner
        robot.attack(dinosaur)
        while (dinosaur.health >=1):
            continue
        else: 
            winner == robot
            self.display_winner


    def display_winner(self, winner):
        #witty response
        print(f"{winner} executes a crushing blow. {winner} WINS!!")
        return








