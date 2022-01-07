import turtle
def rajz(hossz, szog, oldal):
    for i in range(oldal):
        turtle.forward(hossz)
        turtle.left(szog)

rajz(100, 120, 3)
rajz(100, 90, 4)
rajz(100, 60, 6)
rajz(50, 20, 18)