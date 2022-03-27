import turtle
import random
import operator
import math

myTurtle, tX, tY, tColor, tSize, tShape, tSum, tAngle = [None] * 8
playerTurtles = []
swidth, sheight = 500, 500
    
#2021041040 강문정
if __name__ == "__main__" :
    turtle.title('거북이 리스트')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random();
        g = random.random();
        b = random.random();
        tSize = random.randrange(1, 100)/10
        tSum = tX + tY
        tAngle=random.randrange(0, 361)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tSum, tAngle])

    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[8], reverse = True)

    for index, tList in enumerate(sortedTurtles[0:]):
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        
        if index == 0:
            myTurtle=tList[0]
            myTurtle.pendown()
            myTurtle.goto(tList[1], tList[2])
        else:
            myTurtle.goto(tList[1], tList[2])
            myTurtle.goto(sortedTurtles[index][1],sortedTurtles[index][2])
            myTurtle.pendown()
            myTurtle.goto(tList[1], tList[2])
turtle.done()
