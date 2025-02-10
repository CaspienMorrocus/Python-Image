import turtle
import random
import math

t = turtle.Turtle()
window = turtle.Screen()
t.speed(0)

WIN_width = 512
WIN_length = 512

bg_color = ['#cae3e7', '#000D48']

bg_num = random.randint(0, 1)
print(bg_num)

t.screen.setup(WIN_width, WIN_length)
t.screen.bgcolor(bg_color[bg_num])

t.pu()
t.goto(-124, 100)
t.pd()

#'#ffa8b0'
#'#c6dfe4'
#'#d7d3e3'

def bg_layers(m_color, l1_color, l2_color):
    t.color(m_color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.color(l1_color)
    t.pu()
    t.goto(0,0)
    t.pd()
    t.begin_fill()
    t.fd(256)
    t.rt(90)
    t.fd(256)
    t.rt(90)
    t.fd(512)
    t.rt(90)
    t.fd(256)
    t.rt(90)
    t.fd(256)
    t.end_fill()

    t.penup()
    t.goto(-256, -256)
    t.pendown()

    t.color(l2_color)

    t.begin_fill()
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(512)
    t.rt(90)
    t.fd(512)
    t.rt(90)
    t.fd(512)
    t.rt(90)
    t.fd(512)
    t.end_fill()

if bg_num == 0:
    bg_layers('#ffa8b0', '#c6dfe4', '#d7d3e3')
else:
    bg_layers('#8f919a', '#000829', '#00051c')

t.penup()
t.goto(-512, -512)
t.pendown()

morn_colors = ['#ffa8b0', '#fedcc0', '#ffe6c7', '#fea7af']
nig_colors = ['#1b2452', '#243171', '#21348e', '#21348e']

if bg_num == 0:
    colors = morn_colors
else: 
    colors = nig_colors


def circle(num):
    for i in range(num):
        t.begin_fill()
        c = random.randint(0, 3)
        t.color(colors[c])
        x = random.randint(-256, 512)
        y = random.randint(-256, -100)
        c_radius = random.randint(50, 100)
        t.pu()
        t.goto(x, y)
        t.pd()
        t.circle(c_radius)
        t.end_fill()
    
circle(50)

t.pu()
t.goto(-256, -256)
t.pd()



MAX_SLOPE = 45
MIN_SLOPE = -45
MIN_HEIGHT = -256
def dist_squared(P1,P2):
    return (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2

def mountain(P1,P2):
    if dist_squared(P1,P2) < 9:
        turtle.goto(P2)
        return
    x1,y1 = P1
    x2,y2 = P2
    x3 = random.uniform(x1,x2)
    y3_max = min((x3-x1)*math.tan(math.radians(MAX_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MIN_SLOPE)) + y2)
    y3_min = max((x3-x1)*math.tan(math.radians(MIN_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MAX_SLOPE)) + y2)
    y3_min = max(y3_min, MIN_HEIGHT)
    y3 = random.uniform(y3_min,y3_max)
    P3 = (x3, y3)
    mountain(P1,P3)
    mountain(P3,P2)
    return  

turtle.up()


def draw_mount():
    turtle.goto(-256,MIN_HEIGHT)
    turtle.down()
    turtle.color('#6e89a4')
    turtle.begin_fill()
    mountain((-256,-150),(256,68))
    turtle.goto(256, -256)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-256, MIN_HEIGHT)
    turtle.pendown()
    turtle.color('#769ab2')
    turtle.begin_fill()
    mountain((-256,MIN_HEIGHT),(256,56))
    turtle.goto(256, MIN_HEIGHT)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-256, MIN_HEIGHT)
    turtle.pendown()
    turtle.color('#8bb3bf')
    turtle.begin_fill()
    mountain((-256,MIN_HEIGHT),(256,-86))
    turtle.goto(256, MIN_HEIGHT)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-256, MIN_HEIGHT)
    turtle.pendown()
    turtle.color('#6f8aa5')
    turtle.begin_fill()
    mountain((-256,MIN_HEIGHT),(256,MIN_HEIGHT))
    turtle.end_fill()
draw_mount()


def buttonclick(x, y):
    print('You clicked at: ({0}, {1})'.format(x, y))
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.speed(10)
turtle.done()

try:
    window.exitonclick()
except turtle.Terminator:
    pass


