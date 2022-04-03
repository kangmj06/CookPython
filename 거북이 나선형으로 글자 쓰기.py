import turtle
import random
from tkinter.simpledialog import *
import math

inStr=''
count,i=0,0
count=len(inStr)

swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20
radius, angle, radian = 200, 0, 0

turtle.title('거북이 나선형으로 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
angle = 360*2 / len(inStr)
#이름: 강문정 학번: 2021041040
for i in range(0,count):
    radian = 3.14*angle/180
    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.goto(tX, tY)
    turtle.pencolor((r, g, b))
    turtle.write(i, font=('맑은 고딕', txtSize, 'bold'))
    angle+=360*2 / len(count)
    
turtle.done()
