import math

# Função que desenha um quadrado.
def quadrado(t, comprimento):

    for i in range(4):
        t.forward(comprimento)
        t.left(90)


# Função que desenha um polígono regular.
# n = número de lados.
# O ângulo externo de um polígono regular é 360 / n.
def poligono(t, comprimento, n):

    angulo = 360 / n

    for i in range(n):
        t.forward(comprimento)
        t.left(angulo)


# Função que desenha um círculo aproximado usando vários lados pequenos.
# Circunferência do círculo: C = 2πr
# comprimento * n = circunferência
def circulo(t, raio):

    n = 60
    circunferencia = 2 * math.pi * raio
    comprimento = circunferencia / n

    poligono(t, comprimento, n)


# Função que desenha apenas parte de um círculo 

def arco(t, raio, angulo):

    comprimento_arco = 2 * math.pi * raio * angulo / 360

    n = 60
    passo_comprimento = comprimento_arco / n
    passo_angulo = angulo / n

    for i in range(n):
        t.forward(passo_comprimento)
        t.left(passo_angulo)