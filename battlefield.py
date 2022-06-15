from dinosaur import Dinosaur
from robot import Robot

# import random #??

class Battlefield:
    def __init__(self, name):
        self.name = name
        self.robot = Robot("Megatron")
        self.dinosaur = Dinosaur("T-rex", "tailsweep")
        self.winner = ()
    



      

    def display_welcome(self, robot, dinosaur):
        #witty welcome (hype it up!)
        print(f"{robot.name} thunks into the {self.name}. Its {self.robot.active_weapon.name} at the ready. ")
        print(f"{dinosaur.name} stomps into the {self.name}. Its tail lashing threateningly.")

        print(f"Welcome to the epic battle of ROBOT vs DINOSAUR!!!")
        print(f"Today we have {robot.name} and {dinosaur.name}.")
        print(f"Ready...Set...FIGHT!")
        self.battle_phase(self.robot, self.dinosaur)
        return #or continue?



    def display_winner(self, winner):
        #witty response
        print(f"{self.winner} executes a crushing blow. {self.winner} WINS!!")
        return


    def battle_phase(self, robot, dinosaur):
        #loop until at zero or lower

        self.dinosaur.attack(robot)
        while (self.robot.health <= 0):
            self.winner = self.dinosaur
            self.display_winner(self.winner)
            return
        while (self.robot.health > 0):
            print(f"{self.robot.name} is still standing!") 
            print()
            break

        self.robot.attack(dinosaur)
        while (self.dinosaur.health <= 0):
            self.winner = self.robot
            self.display_winner(self.winner)
            return
        while (self.dinosaur.health > 0): 
            print(f"{self.dinosaur.name} is still standing!") 
            return
    

    def run_game(self):
        print()
        #call display_welcome
        self.display_welcome(self.robot, self.dinosaur)
        print()
        #call battle_phase & loop until zero or lower
        self.battle_phase(self.robot, self.dinosaur)
        print()
        #call display_winner
        self.display_winner(self.winner)




