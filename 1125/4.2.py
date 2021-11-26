import turtle
kaloz =  [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in kaloz:
    turtle.left(i)
    turtle.forward(100)
print(turtle.heading())