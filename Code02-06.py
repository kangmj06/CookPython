import turtle


##함수 선언 부분##

##변수 선언 부분##
myT=None

##메인 코드 부분##
myT=turtle.Turtle() #제목
myT.shape('turtle')

for i in range(0,4):
    myT.forward(200)
    myT.right(90)

myT.done()


