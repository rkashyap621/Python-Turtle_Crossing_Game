from turtle import Turtle

class PlayerTurtle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.position = position
        self.player_speed = 10


    def create_turtle(self):
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.shape('turtle')
        self.color('white')
        self.goto(self.position)
        self.setheading(90)
        self.showturtle()


    def move_up(self):
        self.forward(self.player_speed)
