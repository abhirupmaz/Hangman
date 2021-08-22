from turtle import *
class StatusBar(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,-300)
        self.pencolor("white")
        

    def guess_letter(self):
        self.clear()
        self.write("Guess a letter!",align="center",font=("Arial", 15, "normal"))
        

    def correct_guess(self):
        self.clear()
        self.write("Correct guess!",align="center",font=("Arial", 15, "normal"))
        

    def already_guessed(self,guess):
        self.clear()
        self.write(f"You've already guessed {guess}",align="center",font=("Arial", 15, "normal"))
        

    def wrong_guess(self,guess):
        self.clear()
        self.write(f"You guessed {guess}, that's not in the word. You lose a life.",align="center",font=("Arial", 15, "normal"))
