from turtle import Turtle


# DASHED LINE
class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=-330)
        self.setheading(90)
        self.color("white")
        self.pensize(5)

    def create_line(self):
        for x in range(18):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
