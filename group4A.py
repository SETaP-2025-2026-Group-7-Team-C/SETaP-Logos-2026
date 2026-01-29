import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Helper function to draw a filled circle
def filled_circle(radius, fill_color, outline_color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw coin
filled_circle(120, "grey", "grey")
filled_circle(105, "white", "white")

t.pensize(18)

t.color("green")


t.penup()
t.goto(-50, 0)
t.pendown()

#Correct Mark
t.right(45)
t.forward(60)
t.left(105)
t.forward(120)         

turtle.done()
