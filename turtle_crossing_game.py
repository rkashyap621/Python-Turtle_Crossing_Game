from turtle import Screen
from player_turtle import PlayerTurtle
from car_vehicles import Vehicle
from game_control import GameControl
import time

is_game_on = True
current_level = 1

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 1000, height = 1000)
height = screen.window_height()
width = screen.window_width()
screen.tracer(0)

player = PlayerTurtle((0, -1 * (height / 2) + 20))
player.create_turtle()
game_manager = GameControl()
vehicle = Vehicle()

while is_game_on:

    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(player.move_up, "p")

    vehicle.create_vehicle()
    vehicle.vehicle_movement(current_level)
    game_manager.level_display(current_level)

    if player.ycor() > (height / 2):
        player.setpos(0, -(height / 2))
        current_level += 1

    if vehicle.vehicle_collision(player):
        is_game_on = False
        game_manager.game_over()

screen.exitonclick()
