from turtle import *
class Logo(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.color("white")
        #img=screen.register_shape("logo.gif")
        #sc=screen.getcanvas(img)
        screen.addshape("logo.gif")
        self.shape("logo.gif")