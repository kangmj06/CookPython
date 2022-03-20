import turtle
import random


def screenRightClick(x,y):
    global r,g,b
    turtle.color(r,g,b)
    turtle.pendown()
    turtle.goto(x,y)
    turtle.stamp()
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()



pSize=10
r,g,b=0.0,0.0,0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)


turtle.onscreenclick(screenRightClick,3)

turtle.done()
