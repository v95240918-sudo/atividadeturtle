import turtle
import math

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)


def circle(t, r):
    n = 60
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, length, n)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)