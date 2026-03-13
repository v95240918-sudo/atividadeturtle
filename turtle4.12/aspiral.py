def espiral(t):

    distancia = 1

    for i in range(200):

        t.forward(distancia)
        t.left(20)
        distancia += 0.5