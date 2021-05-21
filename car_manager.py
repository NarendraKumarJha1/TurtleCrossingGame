from turtle import Turtle
import random
COLORS = ["violet", "magenta", "orange", "yellow", "green", "blue", "purple", "cyan", "pink", "skyblue", "turquoise", "lightgreen", "darkgreen", "chocolate", "brown", "maroon"]


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.lvl = 12
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_cars(self):
        random_chance = random.randint(1, self.lvl)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-350, 350)
            new_car.goto(700, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
        self.lvl -= 1

    def reset(self):
        self.lvl = 12
        self.STARTING_MOVE_DISTANCE = 5
