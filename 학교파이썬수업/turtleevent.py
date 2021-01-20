import turtle as t
 
def colorRed() :
    t.pencolor( "red" )
 
def colorBlue() :
    t.pencolor( "blue" )
 
def colorGreen() :
    t.pencolor( "green" )
 
def width1() :
    t.pensize( 1 )
 
def width3() :
    t.pensize( 3 )
 
def width5() :
    t.pensize( 5 )
 
def moveForward( x, y) :
    t.setpos( x, y )
 
def checkpoint() :
    t.stamp()
    t.ontimer( checkpoint, 5000 )
    # 5초 후에 checkpoint 함수로 가기
    # 계속 5초 후에 checkpoint 함수로 가면서 5초에 한번씩 stamp 찍도록 무한 반복해둠
 
def clearAll() :
    t.clear()
 
t.shape( "turtle" )
 
t.onkeypress( colorRed, "r" )
t.onkeypress( colorBlue, "b" )
t.onkeypress( colorGreen, "g" )
 
t.onkeypress( width1, "1" )
t.onkeypress( width3, "3" )
t.onkeypress( width5, "5" )
 
t.onkeypress( clearAll, "Down" )
 
t.onscreenclick( moveForward )
# 누르면 moveForward 함수로 가서 setpos()함수를 통해 클릭한 지점 (x,y)로 이동하기
# setpos() 함수는 이동하기 함수
 
t.ontimer( checkpoint, 5000 )
# 우선 checkpoint함수에 진입하도록 함
# 5초 후 checkpoint 함수로 가기
 
t.listen()
# 작성한 코드들 적용 가능하게 만들어주는 listen() 함수
t.done()
