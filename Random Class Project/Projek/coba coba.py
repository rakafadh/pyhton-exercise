import turtle

# set up the turtle
turtle.speed(10.49)
turtle.pencolor("red")
turtle.fillcolor("yellow")

# draw the petals of the flower
for i in range(36):
    turtle.begin_fill()
    turtle.circle(100, 75)
    turtle.left(110)
    turtle.circle(100, 75)
    turtle.end_fill()
    turtle.left(30)

# hide the turtle
turtle.hideturtle()

# keep the window open until the user closes it
turtle.exitonclick()
