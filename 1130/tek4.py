import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Gyönyörű")
toll = turtle.Turtle()
toll.color("blue")
toll.pensize(1)
toll.speed(1000)
ertek = 0
def spiral():
    for i in range(1):
        toll.forward(ertek)
        toll.right(90)

for i in range(100):
    spiral()
    ertek = ertek + 2

ablak.exitonclick()