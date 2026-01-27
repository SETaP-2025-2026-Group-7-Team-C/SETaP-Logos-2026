import turtle

#Setup Screen

screen = turtle.Screen()
screen.bgcolor = ("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(50)

#Draw Circles

t.penup()
t.goto(0, -120)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(120)
t.end_fill()

t.penup()
t.goto(0, -105)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(105)
t.end_fill()

#Verticle line of D

t.penup()
t.goto(-10,0)
t.color("red")
t.pensize(10)
t.pendown()
t.left(90)
t.forward(80)

t.right(90)
t.circle(-40, 180)




turtle.done()