import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
toll = turtle.Turtle()

def draw_square(t,size):
    for i in range(4):
        toll.forward(size)
        toll.left(90)

size = 20
for j in range(5):
   toll.pensize(3)
   draw_square(toll,size)
   size = size + 20
   toll.penup()
   toll.goto(toll.xcor()-10, toll.ycor()-10)
   toll.pendown()
wn.mainloop
