from turtle import Turtle
import random

color_palette = ["violet", "turquoise", "SkyBlue", "chartreuse", "gold", "tomato", "firebrick"]


class Vehicle(Turtle):


    def __init__(self):
        super().__init__()
        self.vehicle = 0
        self.vehicles = []


    def create_vehicle(self):
        random_choice = random.randint(1, 15)
        if random_choice % 11 ==0:
            self.vehicle = Turtle()
            self.vehicle.penup()
            self.vehicle.speed("slowest")
            self.vehicle.shape("square")
            self.hideturtle()
            self.vehicle.color(random.choice(color_palette))
            self.vehicle.shapesize(stretch_len=4, stretch_wid=2)
            self.vehicle.setheading(180)
            y_cor = random.randint(-350, 350)
            self.vehicle.goto(500, y_cor)
            self.showturtle()
            self.vehicles.append(self.vehicle)


    def vehicle_movement(self, level):
        for vehicle in self.vehicles:
            vehicle.forward(5*level)


    def vehicle_collision(self, p_turtle):
        for vehicle in self.vehicles:
            if vehicle.distance(p_turtle) < 40:
                return True
        return False
