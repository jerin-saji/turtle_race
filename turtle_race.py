from turtle import Turtle,Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race ? Enter a colour")
colours = ['red','orange','yellow','green','blue','purple']
y_positons = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230,y=y_positons[turtle_index])
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winnig_colour = turtle.pencolor()
            if winnig_colour == user_bet:
                print(f"You WON! The {winnig_colour} turtle is the winner!")
            else:
                print(f"You lost! The {winnig_colour} turtle is the winner!")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()