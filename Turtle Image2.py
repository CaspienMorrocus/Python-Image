import turtle
import turtle
import tkinter as tk

# Set up the window
screen = turtle.Screen()

# Get the screen dimensions using tkinter
root = tk.Tk()
root.withdraw()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



#Install Tokyo Hack theme on vs code at home

t = turtle.Turtle()
window = turtle.Screen()
window.tracer(False)
turtle.title('Sunset')
Sun = 'Sun-01.gif'
balloon = 'hotairballoon.gif'


COLOR = (1, 0.412, 0) 
TARGET = (0.741, 0.165, 0.651)

WIN_width = screen_width
WIN_length = screen_height

deltas = [(hue - COLOR[index]) / WIN_length for index, hue in enumerate(TARGET)]

t.screen.setup(WIN_width, WIN_length)
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIN_width/2, WIN_length/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(WIN_length//2, -WIN_length//2, -1)):

    turtle.forward(WIN_width * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

t.color('#eaa170')

t.pu()
t.goto(0, 65)
t.pd()

window.addshape(Sun)
t.shape(Sun)
t.stamp()

t.turtlesize(stretch_wid=100, stretch_len=5)

mount_colors = ['#183267', '#204e85']

def birds(radius, degree, width, color):
    t.color(color)
    t.width(width)
    t.lt(90)
    t.circle(radius, degree)
    t.rt(180)
    t.circle(radius, degree)

def mountain(c, x, y, s):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(c)
    t.begin_fill()
    for i in range(1):
        t.fd(s)
        t.lt(120)
        t.fd(s)
        t.lt(120)
        t.fd(s)
    t.end_fill()
    t.lt(120)
    t.fd(s)

mountain('#e7eeff', -450, -214, 300)
mountain('#e7eeff', -150, -214, 300)
mountain('#e7eeff',  150, -214, 300)
mountain('#84a3e1',  -300, -214, 300)
mountain('#84a3e1',  0, -214, 300)
mountain('#2d598f',  -400, -214, 200)
mountain('#2d598f',  -200, -214, 200)
mountain('#2d598f',  0, -214, 200)
mountain('#2d598f',  200, -214, 200)

t.pu()
t.goto(-279, 130)
t.pd()

birds(25, 150, 3, 'black')
t.setheading(0)

t.pu()
t.goto(-175, 170)
t.pd()

birds(25, 200, 3, 'black')
t.setheading(0)

t.pu()
t.goto(-251.0, 90.0)
t.pd()


birds(25, 200, 3, 'black')
t.setheading(0)

t.pu()
t.goto(139, 52)
t.pd()

window.addshape(balloon)
t.shape(balloon)
t.stamp()

window.tracer(True)

def buttonclick(x, y):
    print('You clicked at: ({0}, {1})'.format(x, y))
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.speed(10)
turtle.done()

try:
    turtle.exitonclick()
except turtle.Terminator:
    pass 
