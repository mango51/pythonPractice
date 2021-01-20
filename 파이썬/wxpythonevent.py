import wx
 
app = wx.App() #wx 모듈 불러오기
frame = wx.Frame( None ) #프레임에 아무 속성 넣어도 상관없음
 
def onButtonClick( event ) : #이벤트 작동하면
    print( "x좌표 : ", event.x )
    #이벤트가 작동한 (마우스 클릭한 위치) x좌표 출력
    #event.x = 해당 이벤트에서 우리가 필요한 정보 (x좌표) 가져옴
    print( "y좌표 : ", event.y ) #여기는 y좌표 출력
frame.Bind( wx.EVT_LEFT_DOWN, onButtonClick ) 
#프레임에서 이벤트 마우스 왼쪽 클릭시 함수 onButtonClick 작동
#이벤트 코드 앞에서 wx. 붙여야함 >> wx모듈에서 가져온 기능들이니까
 
def onKeyClick( event ) :
    print( "누른 자판 : ", chr(event.KeyCode) ) #누른 자판이 뭔지 출력
    # event.KeyCode = 이벤트 작동시의 받은 아스키코드(문자값)
    # event.KeyCode = 해당 이벤트에서 우리가 필요한 정보 (KeyCode) 가져옴
    # chr(event.KeyCode) = 이벤트 작동시 받은 값(문자값)을 문자로 변환
frame.Bind( wx.EVT_CHAR, onKeyClick )
# 프레임에서 자판 누르면(이벤트 작동시) 함수 onKeyClick작동
#이벤트 코드 앞에서 wx. 붙여야함 >> wx모듈에서 가져온 기능들이니까
 
frame.Show( True ) #프레임 보여주라
app.MainLoop() #프레임 끄지 마라

# event.정보 = 해당 event에서 우리가 필요한 정보 가져옴
# event.x = 현재 마우스가 눌린 위치의 x좌표
# event.y = 현재 마우스가 눌린 위치의 y좌표 
# event.KeyCode = 현재 눌린 자판의 아스키코드 (문자값)
# chr(event.KeyCode) => 아스키코드(event.KeyCode)를 문자로 바꿔주는 chr()함수
