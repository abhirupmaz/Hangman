from turtle import *

class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,-200)
        self.pencolor("white")
        self.display=[]

    def make_dashes(self,word):
        for _ in range(len(word)):
            self.display += "_"
    
    def show_dashes(self):
        self.write(f"{' '.join(self.display)}",align="center",font=("Arial", 20, "normal"))

    def update_dash(self,position,letter):
        self.display[position] = letter         
