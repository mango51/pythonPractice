import turtle
import random

#전역 변수 선언 부분
myTurtle, tX, tY,tColor,tSize,tShape = [None]*6
shapeList=[]
playerTurtles=[] #2차원 리스트 (거북이 100마리 저장)
swidth,sheight=500,500

#메인 코드 부분
if __name__=='__main__':
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50,height=sheight+50)
    #화면 틀 크기 설정
    turtle.screensize(swidth,sheight)
    #실행창 크기 설정

    shapeList=turtle.getshapes()
    #shapeList=['arrow','blank','circle','classic','square','triangle','turtle']
    #모듈 turtle에서 getshapes()함수를 통해 shape 종류 리스트를 shapeList에 대입하기

    for i in range(0,100): #거북이 100마리를 1차원 리스트로 생성
        random.shuffle(shapeList) #shuffle() : 리스트의 요소 순서를 무작위로 섞음
        myTurtle=turtle.Turtle(shapeList[0]) #myTurtle : 거북이 개체 생성
        tX=random.randrange(-swidth/2, swidth/2) #tX,tY : 거북이 위치 생성
        tY=random.randrange(-sheight/2,sheight/2) #turtle프로그램은 중간이 (0,0)
        r=random.random();g=random.random();b=random.random() #r,g,b : 거북이 색상 생성
        tSize=random.randrange(1,3) # tSize : 거북이 크기 생성
        playerTurtles.append([myTurtle,tX,tY,tSize, r,g,b]) # playerTurtles에 1차원 리스트 추가
        #2차원 리스트 playerTurtles (100마리 거북이 정보 저장된 2차원 배열 리스트 playerTurtles)

    for tList in playerTurtles: #거북이를 playerTurtles에서 하나씩 추출해 tList에 넣고 반복
        #2차원 배열인 playerTurtles에서 (1차원 배열) 리스트 하나씩 넘겨받아서 실행
        myTurtle=tList[0] #거북이 shape
        myTurtle.color((tList[4],tList[5],tList[6])) #거북이 r,g,b 색상
        myTurtle.pencolor((tList[4],tList[5],tList[6])) #펜 동일 색상
        myTurtle.turtlesize(tList[3]) #거북이 크기
        myTurtle.goto(tList[1],tList[2]) #거북이 위치로 이동

    turtle.done()
