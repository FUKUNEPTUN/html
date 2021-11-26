import turtle
def rajz(hossz, szog, oldal):
    for i in range(oldal):
        turtle.forward(hossz)
        turtle.left(szog)

rajz(50, 20, 18)