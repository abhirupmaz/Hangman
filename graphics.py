from turtle import *

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Hangman")
tim=Turtle()
tim.hideturtle()
tim.pencolor('white')

def stand():
    tim.setheading(90)
    for _ in range(9):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.left(90)
    tim.forward(150)
    tim.backward(40)
    tim.left(90)
    tim.forward(50)

def head():
    tim.circle(15)

def body():
    tim.forward(70)
    tim.backward(50)

def left_arm():
    tim.left(45)
    tim.forward(20)
    tim.backward(20)

def right_arm():    
    tim.right(90)
    tim.forward(20)
    tim.backward(20)

def left_leg():
    tim.setheading(270)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    tim.left(45)
    tim.forward(20)
    tim.backward(20)
    
def right_leg():
    tim.right(90)
    tim.forward(20)
    tim.penup()    

stand()
call=[head,body,left_arm,right_arm,left_leg,right_leg]
for i in range(0,6):
    call[i]()

screen.exitonclick()