import turtle

ablak = turtle.Screen()
toll = turtle.Turtle()
ablak.screensize(10000)
toll.speed(1000)
def csillag(): 
    for i in range(5):
        for i in range(5):
            toll.forward(100)
            toll.right(144)
        toll.forward(400)
        toll.right(144)
csillag()
ablak.mainloop()