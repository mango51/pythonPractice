import turtle
import random

#전역 변수 선언
swidth, sheight, pSize, exitCount = 300,300,3,0
r,g,b,angle,dist,curX,curY = [0]*7
#윈도우창의 크기 (swidth, sheight), 펜의 두께(pSize), 윈도우 밖으로 나간 횟수(exitCount)의 초기화
#색상(r,g,b), 각도(angle), 거리(dist)는 random하게 설정됨
#현재 거북이의 위치 (curX, curY)


#메인 코드 부분
turtle.title('거북이 마음대로 다니기')
turtle.shape('turtle') #거북이 모양 설정
turtle.pensize(pSize) #펜 두께(pSize = 3으로) 설정
turtle.setup(width=swidth+30, height=sheight+30) #윈도우 크기 설정 (width = 300 + 30 = 330 과 height = 300 +30 = 330)
turtle.screensize(swidth,sheight) #안쪽 화면 설정 (300,300)
#turtle모듈 안의 함수들 사용함 >> turtle.turtle모듈안의함수()

#거북이 임의로 이동 (무한 반복)
while True: #무한반복
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b)) #펜 색상 random()함수 적용된 r,g,b

    angle = random.randrange(0,360) #움직이는 각도 자유자재 (제한된 범위 내에서)
    dist = random.randrange(1,100) #움직이는 거리 자유자재 (제한된 범위 내에서)
    turtle.left(angle) #왼쪽으로 꺾되 각도는 자유자재 > 아무대나 턴할 수 있음 0~360도
    turtle.forward(dist) #앞으로 가되 거리는 정해진 범위 내에서 자유자재 > 거리는 1~100 
    curX = turtle.xcor() #x좌표는 0 (전역변수값, 초기값) = 현재위치
    curY = turtle.ycor() #y좌표는 0 (전역변수값, 초기값) = 현재위치
    #xcor는 turtle 모듈에서 현위치 표현 함수

    if (-swidth/2 <= curX and curX <= swidth/2) and (-sheight/2 <= curY and curY <= sheight/2): #안쪽 화면 내에 있을 때
        #-swidth/2는 -150으로 x=-150 (300,300인 안쪽 화면 중가운데를 (0,0)에 배치함) 맨 왼쪽 가장자리는 x=-150
        #swidth/2는 150으로 x=150 맨 오른쪽 가장자리는 x=150임
        #거북이가 안쪽 화면 밖으로 나갈때는 거북이 현 x 위치 < -150이거나 (and) 거북이 현 y 위치 > 150임 : 이러기에 조건문 위와 같음
        pass #명령문 쓸 일 없을 때, 할일 없을 때 pass 사용
        #pass 적용시 if문 종료하고 다시 while문 처음부터 시작
    else:
        turtle.penup() #펜을 올려서 작성하지 말구
        turtle.goto(0,0) #거북이를 (0,0)에 가기
        turtle.pendown() #펜을 다시 내려서 작성하도록 하기

        exitCount += 1 #나갈 때마다 exitCount에 1더하기
        if exitCount >= 5:
            break #5번 이상 나가면 break로 무한 반복 그만두기

turtle.done() #프로그램 끝내기
#맨 마지막에 전체 코드 겉을 아우르는 형식으로 프로그램 끝내는 done() 함수 적용
