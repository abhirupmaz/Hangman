import random
from hangman_words import word_list
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

dash=Dash()

call=[graphics.right_leg, graphics.left_leg, graphics.right_arm, graphics.left_arm, graphics.body, graphics.head]

game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

status_bar.guess_letter()

dash.make_dashes(chosen_word)
dash.show_dashes()

while not game_is_finished:

    guess = textinput('Hangman','Guess a letter: ').lower()

    if guess in dash.display:
        status_bar.already_guessed(guess)

    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                dash.update_dash(position,letter)
                status_bar.correct_guess()
    dash.clear()
    dash.show_dashes()

    if guess not in chosen_word:
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