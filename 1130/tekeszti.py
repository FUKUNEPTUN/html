import turtle
ablak = turtle.Screen()
Eszti = turtle.Turtle()

Eszti.color("black")
Eszti.pensize(1)
def sokszog_rajzolas(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360 // n)
sokszog_rajzolas(Eszti, 8, 50)
ablak.mainloop()

        
    