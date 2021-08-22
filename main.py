from statusbar import StatusBar
from graphics import Graphics
from dashes import Dash
from turtle import *
from finaloutput import Message

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Hangman")

graphics=Graphics()

message=Message()

status_bar=StatusBar()
turtle=Turtle()
turtle.hideturtle()
turtle.goto(0,-200)
turtle.pencolor("white")
dash=Dash()
#turtle=Turtle()
#turtle.hideturtle()
#turtle.goto(0,-200)
#turtle.pencolor("white")

#turtle1=Turtle()
#turtle1.hideturtle()
#turtle1.goto(0,-250)
#turtle1.pencolor("white")


call=[graphics.right_leg, graphics.left_leg, graphics.right_arm, graphics.left_arm, graphics.body, graphics.head]
import random
from hangman_words import word_list

game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
#word_length = len(chosen_word)

#display = []
#for _ in range(word_length):
#    display += "_"

<<<<<<< HEAD

turtle.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))
#turtle1.write("Guess a letter!",align="center",font=("Arial", 10, "normal"))
status_bar.guess_letter()

=======
dash.make_dashes(chosen_word)
dash.show_dashes()
#dash.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))
turtle1.write("Guess a letter!",align="center",font=("Arial", 10, "normal"))
>>>>>>> 4e4388da21e0980118340f8df2d86d7b6535964a
while not game_is_finished:
    # guess = input("Guess a letter: ").lower()
    guess = textinput('Hangman','Guess a letter: ')

    if guess in dash.display:
        # print(f"You've already guessed {guess}")
<<<<<<< HEAD
        # turtle1.clear()
        # turtle1.write(f"You've already guessed {guess}",align="center",font=("Arial", 10, "normal"))
        status_bar.already_guessed(guess)

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                # turtle1.clear()
                # turtle1.write("Correct guess!",align="center",font=("Arial", 10, "normal"))
                status_bar.correct_guess()


    turtle.clear()
    turtle.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))    
=======
        turtle1.clear()
        turtle1.write(f"You've already guessed {guess}",align="center",font=("Arial", 10, "normal"))
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                dash.update_dash(position,letter)
                #display[position] = letter
                turtle1.clear()
                turtle1.write("Correct guess!",align="center",font=("Arial", 10, "normal"))
            
    dash.clear()
    dash.show_dashes()
    #dash.write(f"{' '.join(display)}",align="center",font=("Arial", 20, "normal"))    
>>>>>>> 4e4388da21e0980118340f8df2d86d7b6535964a
    # print(f"{' '.join(display)}")

    if guess not in chosen_word:
        # print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # turtle1.clear()
        # turtle1.write(f"You guessed {guess}, that's not in the word. You lose a life.",align="center",font=("Arial", 10, "normal"))
        status_bar.wrong_guess(guess)

        lives -= 1
        call[lives]()
        if lives == 0:
            game_is_finished = True
            message.losing_message()
    
    if not "_" in dash.display:
        game_is_finished = True
        message.winning_message()

screen.exitonclick()