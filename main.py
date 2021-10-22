from turtle import Screen
from dash import Dash
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from random import choice
import time

paddle_colors = [(231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226),
                  (30, 110, 159), (235, 81, 44), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144),
                  (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24),
                  (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68),
                  (227, 171, 162), (73, 135, 188), (172, 204, 174)]

# SCREEN SET UP
screen = Screen()
screen.title("It's pong time")
screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.tracer(0)

# DASHED LINE
dash = Dash()
dash.create_line()

# OBJECTS
scoreboard = Scoreboard()
right_paddle = Paddle()
left_paddle = Paddle()
left_paddle.goto(x=-470, y=0)
ball = Ball()

# LISTEN
screen.listen()
screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")
screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")

# GAME TIME
game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 335 or ball.ycor() < -335:
        ball.bounce_y()

    # collision with right paddle
    if ball.xcor() >= 450 and ball.distance(right_paddle) < 50:
        right_paddle.color(choice(paddle_colors))
        ball.bounce_x()

    # collision with left paddle
    if ball.xcor() <= -450 and ball.distance(left_paddle) < 50:
        left_paddle.color(choice(paddle_colors))
        ball.bounce_x()

    # left score
    if ball.xcor() >= 480:
        ball.ball_reset()
        scoreboard.increase_left_score()

    # right score
    if ball.xcor() <= -480:
        ball.ball_reset()
        scoreboard.increase_right_score()

    # check if left wins
    if scoreboard.left_score > 11:
        scoreboard.goto(0, 0)
        scoreboard.write("Left Player Wins!", False, "center", ("Arial", 50, "normal"))
        game_on = False

    # check if right wins
    if scoreboard.right_score > 11:
        scoreboard.goto(0, 0)
        scoreboard.write("Right Player Wins!", False, "center", ("Arial", 50, "normal"))
        game_on = False

screen.exitonclick()
