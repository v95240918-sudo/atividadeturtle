import turtle
from flores import flor
from tortas import torta
from espiral import espiral

bob = turtle.Turtle()

flor(bob, 60, 7, 60)

bob.penup()
bob.goto(200,0)
bob.pendown()

torta(bob, 6, 80)

bob.penup()
bob.goto(-200,-100)
bob.pendown()

espiral(bob)

turtle.done()