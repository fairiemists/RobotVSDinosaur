from dinosaur import Dinosaur
from robot import Robot

# import random #??

class Battlefield:
    def __init__(self, name):
        self.name = name
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    
    
    dinosaur_one = Dinosaur("T-rex:", "tailsweep")
    # print witty creation comment
    print(f"{dinosaur_one} stomps into the {self.name}. ")
    
    
    # create robot (Fleet class?)
    robot_one = Robot("Megatron")
    # print witty creation comment
    print(f"{robot_one} thunks into the {self.name}. Its {robot.weapon_one} at the ready. ")

      

    def display_welcome(self, robot, dinosaur):
        #witty welcome (hype it up!)
        print(f"Welcome to the epic battle of ROBOT vs DINOSAUR!!!")
        print(f"Today we have {robot} and {dinosaur}.")
        print(f"Ready...Set...FIGHT!")
        self.battle_phase()
        return #or continue?



    def display_winner(self, winner):
        #witty response
        print(f"{winner} executes a crushing blow. {winner} WINS!!")
        return


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




