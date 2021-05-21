from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-600, 360)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0