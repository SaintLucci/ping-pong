from turtle import Turtle
import random

RAND_ANGLE = random.randint(120, 240)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_x = 5
        self.move_y = 5
        self.ball_speed = .02

    def create_ball(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(RAND_ANGLE)
        self.speed("fastest")
    
    def detected_collision(self, position):
        if self.ball.distance(position) < 50:
            return True
        else:
            return False

    def move_ball(self):
        self.ball.goto(self.ball.xcor() + self.move_x, self.ball.ycor() + self.move_y)

    def bounce_x(self):
        self.move_x *= -1
        self.ball_speed *=0.9

    def bounce_y(self):
        self.move_y *= -1
        self.ball_speed *=0.9

    def get_x(self):
        return self.ball.xcor()

    def get_y(self):
        return self.ball.ycor()

