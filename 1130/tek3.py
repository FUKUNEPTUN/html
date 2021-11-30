import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Gyönyörű")
toll = turtle.Turtle()
toll.color("blue")
toll.pensize(3)
toll.speed(100)

def spiral():
    for i in range(4):
        toll.forward(150)
        toll.left(90)

for i in range(20):
    spiral()
    toll.left(18)
ablak.exitonclick()