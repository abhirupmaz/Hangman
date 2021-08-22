from turtle import *
import random

lose=["Nice try but you lose! :(","That's the best you got? Better luck next time :)", "So close yet so far! You Lose!", "You lose but again great attempt!"]
win=["GGWP! You Win!", "Alright smartypants, you win!", "You beautyyyyy! That's how you win!", "Inshallah, the boy played well!"]

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0,200)
    
    def winning_message(self):
        self.write(random.choice(win),align="center",font=("Arial", 25, "normal"))

    def losing_message(self):
        self.write(random.choice(lose),align="center",font=("Arial", 25, "normal"))
