import turtle
import math
import random

#전역 변수 선언하기
t1,t2,t3 = [None]*3 # None으로 비어둠
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] *6
swidth, sheight= 300,300

#메인 코드 부분
if __name__ == '__main__':
    turtle.title('거북 만나기')
    turtle.setup(width=swidth+50, height= sheight+50)
    turtle.screensize(swidth, sheight)

    # turtle.Turtle() : 거북이 생성, color() : 색상 설정, penup(): 선 그리지 않기
    t1 = turtle.Turtle('turtle'); t1.color('red');t1.penup()
    t2 = turtle.Turtle('turtle');t2.color('green');t2.penup()
    t3= turtle.Turtle('turtle'); t3.color('blue');t3.penup()

    t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)
    #goto()로 거북이 3마리 위치 서로 다르게 설정

    t1.speed(10);t2.speed(10);t3.speed(10) #speed()로 거북이 속도 설정

    while True: #거북이 만날 때까지 무한 반복
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t1.left(angle);t1.forward(dist)
        # 각도와 거리를 임의로 추출해 각 t1 이동시킴
        # t1,t2,t3 각각 다르게 angle, dist 설정한 이유는 하나의 angle, dist 설정하면 함께 움직임
        # angle =... dist= ... t1.left(angle); t1.forward(dist) \ t2.left(angle); t2.forward(dist) \ t3.left(angle); t2.forward(dist)
        # 위의 코드와 같이 할 경우, 하나의 angle과 dist 가지고 있기에 세 개의 거북이가 한꺼번에 같은 방향 각도로 이동
        
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t2.left(angle); t2.forward(dist)
        # 각도와 거리를 임의로 추출해 각 t2 이동시킴

        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t3.left(angle); t3.forward(dist)
        # 각도와 거리를 임의로 추출해 각 t3 이동시킴

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()
        # 각 거북이의 현재 위치를 추출

        if math.sqrt(((t1X-t2X) * (t1X-t2X)) + ((t1Y-t2Y)*(t1Y-t2Y))) <= 20 or \
            math.sqrt(((t1X-t3X) * (t1X-t3X)) + ((t1Y-t3Y)*(t1Y-t3Y))) <= 20 or \
            math.sqrt(((t2X-t3X) * (t2X-t3X)) + ((t2Y-t3Y)*(t2Y-t3Y))) <= 20 :
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            # 두 마리 이상의 거북이 끼리 거리 20미만이면 3마리 모두 거북이 크기 3으로 커짐
            # math 모듈의 sqrt() 함수 사용 >> sqrt() : 수식 계산하는 함
            # (X2 - X1)(X2-X1) + (Y2-Y1)(Y2-Y1)로 피타고라스 공식으로 거리 계산
            # 두 마리 이상의 거북이가 20미만의 거리에 있을 경우
            break
            # 무한 루프 정지 (프로그램 끝)
turtle.done()
            
            
