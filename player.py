from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(outline=5)
        self.color("red")
        self.left(90)
        self.goto_pos()

    def goto_pos(self):
        self.penup()
        self.goto(0, -380)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto_pos()