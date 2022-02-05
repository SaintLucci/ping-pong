from turtle import Turtle

class Paddle:
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.create_paddle(self.pos)

    def create_paddle(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.goto(position)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)

    def reset_position(self):
        self.paddle.goto(self.pos)