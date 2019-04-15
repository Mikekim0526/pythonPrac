import turtle
import random

turtle.colormode(255)

t1= turtle.Turtle()
t1.shape("arrow")
t1.shapesize(1)
t1.speed(100)
t1.width(20)
t1.pencolor(0, 0, 255)

size =int(turtle.textinput("Size", "Input the length"))
angle=int(turtle.textinput("Figure", "Input the angle number"))

for j in range(0, size, 5):
    t1.pendown()
    for i in range(1, angle+1,1):
        t1.forward(size-j)
        t1.right(360/angle)
        r=int(j*255/size)
        b=255-r
        t1.pencolor(r, 0, b)
        g=random.randint(0, 255)
    t1.penup()
    t1.goto(j/2,-2*j)
