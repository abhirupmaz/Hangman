from graphics import Graphics
from turtle import *

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Hangman")

graphics=Graphics()
turtle=Turtle()
turtle.hideturtle()
turtle.goto(0,-200)
turtle.pencolor("white")

turtle1=Turtle()
turtle1.hideturtle()
turtle1.goto(0,-250)
turtle1.pencolor("white")

turtle2=Turtle()
turtle2.hideturtle()
turtle2.goto(0,200)

call=[graphics.right_leg, graphics.left_leg, graphics.right_arm, graphics.left_arm, graphics.body, graphics.head]
import random
from hangman_words import word_list

game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"


turtle.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))
turtle1.write("Guess a letter!",align="center",font=("Arial", 10, "normal"))
while not game_is_finished:
    guess = input("Guess a letter: ").lower()


    if guess in display:
        # print(f"You've already guessed {guess}")
        turtle1.clear()
        turtle1.write(f"You've already guessed {guess}",align="center",font=("Arial", 10, "normal"))

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            turtle1.clear()
            turtle1.write("Correct guess!",align="center",font=("Arial", 10, "normal"))
    turtle.clear()
    turtle.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))    
    # print(f"{' '.join(display)}")

    if guess not in chosen_word:
        # print(f"You guessed {guess}, that's not in the word. You lose a life.")
        turtle1.clear()
        turtle1.write(f"You guessed {guess}, that's not in the word. You lose a life.",align="center",font=("Arial", 10, "normal"))
        lives -= 1
        call[lives]()
        if lives == 0:
            game_is_finished = True
            turtle2.pencolor("red")
            turtle2.write("Good try but you Lose!",align="center",font=("Arial", 25, "normal"))
    
    if not "_" in display:
        game_is_finished = True
        turtle2.pencolor("green")
        turtle2.write("Alright smartypants, you win!",align="center",font=("Arial", 25, "normal"))
        # print("Smartypants, you win!")

screen.exitonclick()