from turtle import *

class Graphics(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.stand()

    def stand(self):
        self.setheading(90)
        for _ in range(9):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.left(90)
        self.forward(150)
        self.backward(40)
        self.left(90)
        self.forward(50)

    def head(self):
        self.circle(15)

    def body(self):
        self.forward(70)
        self.backward(50)

    def left_arm(self):
        self.left(45)
        self.forward(20)
        self.backward(20)

    def right_arm(self):    
        self.right(90)
        self.forward(20)
        self.backward(20)

    def left_leg(self):
        self.setheading(270)
        self.penup()
        self.forward(50)
        self.pendown()
        self.left(45)
        self.forward(20)
        self.backward(20)
        
    def right_leg(self):
        self.right(90)
        self.forward(20)
        self.penup()    

    
    