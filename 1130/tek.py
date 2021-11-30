import turtle
def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""
    for i in range(5):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        t.penup()
        t.forward(sz + (sz))
        t.pendown()

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("red")

    draw_square(alex, 20)

    wn.mainloop()


if __name__ == "__main__":
    main()