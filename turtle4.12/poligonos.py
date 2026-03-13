import math


def poligono(t, comprimento, n):

    angulo = 360 / n

    for i in range(n):
        t.forward(comprimento)
        t.left(angulo)


def circulo(t, raio):

    n = 60
    circunferencia = 2 * math.pi * raio
    comprimento = circunferencia / n

    poligono(t, comprimento, n)


def arco(t, raio, angulo):

    comprimento_arco = 2 * math.pi * raio * angulo / 360

    n = int(comprimento_arco / 4) + 1
    passo_comprimento = comprimento_arco / n
    passo_angulo = angulo / n

    for i in range(n):
        t.forward(passo_comprimento)
        t.left(passo_angulo)