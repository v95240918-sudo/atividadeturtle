import math

def triangulo(t, raio, angulo):

    y = raio * math.sin(math.radians(angulo/2))

    t.forward(raio)
    t.left(180 - angulo/2)
    t.forward(2*y)
    t.left(180 - angulo/2)
    t.forward(raio)


def torta(t, n, raio):

    angulo = 360 / n

    for i in range(n):
        triangulo(t, raio, angulo)
        t.left(angulo)