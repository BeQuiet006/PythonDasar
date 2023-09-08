import turtle

t = turtle.Turtle()
t.speed(0)
sc = turtle.Screen()
sc.setup(800, 500)

t.penup()
t.goto(-400, 250)
t.pendown()

# Red rectangle
t.color("red")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(250)
t.right(90)
t.forward(800)
t.end_fill()

t.hideturtle()
turtle.exitonclick()
