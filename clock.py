import turtle
import time

root=turtle.Turtle()
s=turtle.Turtle()
m=turtle.Turtle()
h=turtle.Turtle()
root.speed(0)
s.speed(0)
s.ht()
h.speed(0)
h.ht()
m.speed(0)
m.ht()
root.ht()
screen=turtle.Screen()
screen.bgcolor("black")
root.pencolor("cyan")

s_angel=90
h_angel=150
m_angel=30

def goto(x=0,y=0,turtle=root):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def circle(size=0,pensize=0):
    goto(0,-330)
    root.setheading(0)
    root.pensize(pensize)
    root.circle(size)


def s_hands(handsize=0,angle=0,color="green",hight=100,heading=0):
    goto(turtle=s)
    s.setheading(heading)
    s.pensize(handsize)
    s.pencolor(color)
    s.left(angle)
    s.forward(hight)

def m_hands(handsize=0,angle=0,color="green",hight=100,heading=0):
    goto(turtle=m)
    m.setheading(heading)
    m.pensize(handsize)
    m.pencolor(color)
    m.left(angle)
    m.forward(hight)

def h_hands(handsize=0,angle=0,color="green",hight=100,heading=0):
    goto(turtle=h)
    h.setheading(heading)
    h.pensize(handsize)
    h.pencolor(color)
    h.left(angle)
    h.forward(hight)


root.left(90)
number=1
root.right(30)
for i in range(12):
    root.up()
    root.forward(300)
    root.right(30)
    root.write(number,font=("comic san ms",30),align="center")
    goto()
    number+=1

circle(size=350,pensize=5)

while True:
    m_hands(handsize=3,angle=m_angel,hight=300,color="blue")
    h_hands(handsize=5,angle=h_angel,hight=250,color="red")
    s_hands(handsize=2,angle=s_angel,hight=300)
    time.sleep(.7)
    s_angel-=6
    s.clear()
    if s_angel==-270:
        s_angel=90
        m_angel-=6
        m.clear()
        if m_angel==-270:
            m_angel=0
            h_angel-=6


turtle.done()