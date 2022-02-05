from turtle import Turtle
ALIGN = "Center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.position = pos
        self.write_score(self.position)

    def write_score(self, pos):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(pos)
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score(self.position)

    def game_over(self, text):
        self.goto(0, 0)
        self.write(text, align=ALIGN, font=FONT)
