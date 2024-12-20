import turtle
from turtle import Turtle , Screen
import random

race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet" , prompt= "Which turtle win the race. Enter a color : ")
colors = ['red','yellow','blue','green','violet','indigo']
y_pos = [-70,-40,-10 , 20,50,80]
turtles = []

for index in range(0,7):
    tim = Turtle(shape = "turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x = -230, y = y_pos[index])
    turtles.append(tim)

if user_bet :
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor()>230:
            winning = turtle.pencolor()
            if winning == user_bet():
                print("You have won!")



            print(turtle.color())



        distance = random.randint(0,10)
        turtle.forward(distance)








screen.exitonclick()