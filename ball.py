import turtle
from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.colors = [(231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226),
                  (30, 110, 159), (235, 81, 44), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144),
                  (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24),
                  (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68),
                  (227, 171, 162), (73, 135, 188), (172, 204, 174)]
        self.penup()
        self.shape("circle")
        self.color(choice(self.colors))
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.06

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.color(choice(self.colors))
        self.ymove *= -1

    def bounce_x(self):
        self.color(choice(self.colors))
        self.xmove *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.xmove = 10
        self.ymove = 10
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.06
