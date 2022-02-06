from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
tim = Turtle()
screen.title("Py Ping Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard_player_one = Scoreboard((-30, 240))
scoreboard_player_two = Scoreboard((30, 240))
player_one_paddle = Paddle((-350, 0))
player_two_paddle = Paddle((350, 0))
#Setting up the screen
tim.penup()
tim.hideturtle()
tim.goto(0, 300)
tim.setheading(270)
tim.color("white")

while tim.ycor() > -300:
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

def ping_pong():
    player_one_paddle.reset_position()
    player_two_paddle.reset_position()
    ball = Ball()
    ball.ball_speed = .001
    is_game_on = True

    screen.listen()
    screen.onkeypress(player_one_paddle.move_up, "Up")
    screen.onkeypress(player_one_paddle.move_down, "Down")

    screen.onkeypress(player_two_paddle.move_up, "w")
    screen.onkeypress(player_two_paddle.move_down, "s")

    while is_game_on:
        screen.update()
        time.sleep(ball.ball_speed)
        ball.move_ball()

        if ball.detected_collision(player_one_paddle.paddle) and ball.get_x() < -340 or ball.detected_collision(player_two_paddle.paddle) and ball.get_x() > 340:
            ball.bounce_x()

        if ball.get_y() > 290 or ball.get_y() < -290:
            ball.bounce_y()

        if ball.get_x() > 400:
            scoreboard_player_one.increase_score()
            ball.clear()
            ping_pong()

        if ball.get_x() < -400:
            scoreboard_player_two.increase_score()
            ball.clear()
            ping_pong()

        if scoreboard_player_one.score == 11:
            is_game_on = False
            scoreboard_player_one.game_over(f"Player one has won.!")
        
        if scoreboard_player_two.score == 11:
            is_game_on = False
            scoreboard_player_two.game_over(f"Player two has won.!")

ping_pong()
screen.exitonclick()

