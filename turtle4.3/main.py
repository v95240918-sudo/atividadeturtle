import turtle
from turtle_formas import quadrado, poligono, circulo, arco

# cria a turtle
bob = turtle.Turtle()

# desenha um quadrado
quadrado(bob, 100)

bob.penup()
bob.goto(200, 0)
bob.pendown()

# desenha um hexágono
poligono(bob, 80, 6)

bob.penup()
bob.goto(-200, 0)
bob.pendown()

# desenha um círculo aproximado
circulo(bob, 60)

bob.penup()
bob.goto(0, -200)
bob.pendown()

# desenha meio círculo
arco(bob, 100, 180)

turtle.done()