from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.left_score = 0
        self.right_score = 0
        self.write(f"{self.left_score}   {self.right_score}", False, "center", ("Arial", 50, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.write(f"{self.left_score}   {self.right_score}", False, "center", ("Arial", 50, "normal"))

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.write(f"{self.left_score}   {self.right_score}", False, "center", ("Arial", 50, "normal"))