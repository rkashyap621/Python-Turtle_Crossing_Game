from turtle import Turtle

class GameControl(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")


    def game_over(self):
        self.home()
        self.write("GAME OVER", align = "center", font = ("Courier", 30, "bold"))


    def level_display(self, level):
        self.clear()
        self.goto(-400, 450)
        self.write(f"Level: {level}", align = "center", font = ("Courier", 20, "bold"))
