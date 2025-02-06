
import turtle


t = turtle.Turtle()
window = turtle.Screen()
window.tracer(False)

COLOR = (1, 0.412, 0)  # (154, 0, 254)
TARGET = (0.741, 0.165, 0.651)

WIN_width = window.window_width()
WIN_length = window.window_height()

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
t.goto(0, -215)
t.pd()




t.begin_fill()
t.circle(230)
t.end_fill()


t.color('#f98334')

t.pu()
t.goto(0, -160)
t.pd()



t.begin_fill()
t.circle(175)
t.end_fill()

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

birds(25, 150, 3, 'white')
t.setheading(0)

t.pu()
t.goto(-175, 170)
t.pd()

birds(25, 200, 3, 'white')
t.setheading(0)

t.color('black')
t.pu()
t.goto(83, 22)
t.pd()
t.width(1)
t.begin_fill()
t.circle(50)
t.end_fill()
t.goto(32, 69)
t.goto(65, -9)
t.begin_fill()
t.goto(65, -31)
t.goto(100, -31)
t.goto(100, -10)
t.goto(65, -9)
t.end_fill()
t.goto(100, -10)
t.goto(132, 69)

window.tracer(True)

def buttonclick(x, y):
    print('You clicked at: ({0}, {1})'.format(x, y))
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.speed(10)
turtle.done()

window.exitonclick()

