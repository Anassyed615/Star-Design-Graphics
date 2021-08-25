## Graphics Design Using Python Turtle

## Python Grapics

import turtle
import random
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor('black')
t.pencolor('orange')
t.speed(50)

def crazy(var1):
    for i in range(700):
        t.forward(i)
        t.left(var1)
crazy(124)
