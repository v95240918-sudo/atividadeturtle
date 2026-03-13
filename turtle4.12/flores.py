from poligonos import arco


def petala(t, raio, angulo):

    arco(t, raio, angulo)
    t.left(180 - angulo)

    arco(t, raio, angulo)
    t.left(180 - angulo)


def flor(t, r, n, angle):

    for i in range(n):
        petala(t, r, angle)
        t.left(360 / n)