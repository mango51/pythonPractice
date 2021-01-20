import turtle

#전역변수 선언하기
num = 0
swidth, sheight = 1000, 300 # 창 크기 
curX, curY = 0,0 # 거북이의 현재 위치

#메인코드
if __name__ == '__main__':
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50) # 창의 크기
    turtle.screensize(swidth, sheight) # 스크린 크기
    turtle.penup() # 그리지 않기 (거북이만 찍어버리기)
    turtle.left(90) # 90도 각도로 왼쪽

    num = int(input('숫자를 입력하세요 : '))

    binary = bin(num)
    # 2진수로 변환해주는 함수 bin()

    #거북이의 초기 위치 설정
    curX = swidth/2 # 화면 중가운데
    curY = 0 # 화면 맨 오른쪽
    # 윈도우창의 오른쪽 끝에서 가운데에 배치

    for i in range(len(binary) -2):
        # 2진수이기 때문에 앞에 0b가 붙는다
        # 따라서 0b를 제외한 2진수를 거북이로 찍을 거기 때문에 0b는 뺀다
        # len(binary)하면 0b포함 크기 나오기에 거기서 -2하기
        turtle.goto(curX, curY) # 거북이 (curX, curY)로 이동하기
        # i=1일 때, left(90)한 상태의 거북이가 오고 goto(curX,curY)를 실행하기
        # i=1일 때, goto(curX,curY)실행해야하기에 위에 선언한 curX=swidth/2, curY=0 가지고와서 실

        if num&1: #맨 하위 비트가 1인지 체크하기 (&1 = 마스크 방식)
            # & 비트 연산자 이기에 num은 2진수로 변환됨
            # 맨 하위 비트가 1이면 &1과 연산하여 1 = True이기에 실행됨
            # 하지만 맨 하위 비트가 0이면 &1과 연산될 때, 0 = False이므로 실행 안됨
            turtle.color('red')
            turtle.turtlesize(2)
            # 위의 두 줄 코드는 맨 하위 비트가 1일 때 실행되는 코드

        else:
            turtle.color('blue')
            turtle.turtlesize(1)
            # 위의 두 줄 코드는 맨 하위 비트가 0일 때 실행되는 코드

        turtle.stamp() # 설정된 크기와 색상으로 거북이 도장 찍기
        curX -= 50 # lef(90)으로 했기에 거북이가 앞으로 (화면에서 왼쪽으로) 50 이동
        # -50한 curX값 설정한 후 for문을 통해 다시 위로 올라갈 때, goto(curX,curY)로 이동하기
        num >>= 1 # 위에서 맨 하위 비트 확인했기에 이제 그 다음 두 번째 하위 비트 확인해야함
        # 따라서 '오른쪽 시프트 연산자'로 두 번째 하위 비트를 맨 하위 비트로 설정
        # 그 다음에 다시 포문 올라가서 마스크 방식으로 다시 또 실행하기

turtle.done()
    
