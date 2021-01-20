import turtle

#전역변수
i,k,tX,tY=[0]*4
swidth, sheight=800,450

#메인 코드
if __name__=='__main__':
    turtle.title('구구단')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    tX,tY=-500,250
    turtle.goto(tX,tY) #(-500,250) 위치로 turtle 가기 (왼쪽 상단)

    for i in range(1,10): #행
        for k in range(2,10): #열
            turtle.goto(tX+80*k,tY-40*i) #거북이 위치 지정 (거북이 해당 위치로 가라)
            gugu=str(k)+'x'+str(i)+'='+str(k*i) 
            turtle.write(gugu,font=('Arial',12,'bold'))
            # turtle이 적어라 gugu 내용 font는 Arial 12폰트, bold체

    turtle.done()
