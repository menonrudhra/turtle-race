from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: red/blue/purple/green/yellow/orange ")
colors = ["purple", "blue", "green", "red", "yellow", "orange"]
FONT = ("Courier", 14, "normal")
all_turtles = []


def initialize_turtle():
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-220, y=-70 + turtle_index * 30)
        new_turtle.color(colors[turtle_index])
        all_turtles.append(new_turtle)


initialize_turtle()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            score = Turtle()
            score.level = 1
            score.hideturtle()
            score.penup()
            score.goto(0, 0)
            if winning_color == user_bet:
                score.write(f"GAME OVER. You have won. The {winning_color} turtle won", align="center", font=FONT)
            else:
                score.write(f"GAME OVER. The winning turtle is {winning_color}. You lose.", align="center", font=FONT)
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
