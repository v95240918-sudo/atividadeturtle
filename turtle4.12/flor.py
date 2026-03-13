from polygon import arc

def petal(t, r, angle):

    arc(t, r, angle)
    t.left(180 - angle)

    arc(t, r, angle)
    t.left(180 - angle)


def flower(t, r, n, angle):

    for i in range(n):
        petal(t, r, angle)
        t.left(360 / n)