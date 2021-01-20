import wx

app=wx.App()
frame=wx.Frame(None)

redRB=wx.RadioButton(frame,label='빨강',style=wx.RB_GROUP)
blueRB=wx.RadioButton(frame,label='파랑')
greenRB=wx.RadioButton(frame,label='초록')

def changeRed(event):
    frame.SetBackgroundColour(wx.Colour(255,0,0,0))
    #배경색상 설정하기 wx.Colour(255,0,0,0)으로
    #wx.Colour(R값,G값,B값,투명도)
    frame.Refresh()
    #배경색상 바꿀 수 있도록 refresh해놓기

def changeBlue(event):
    frame.SetBackgroundColour(wx.Colour(0,0,255,0))
    frame.Refresh()

def changeGreen(event):
    frame.SetBackgroundColour(wx.Colour(0,255,0,0))
    frame.Refresh()

redRB.Bind(wx.EVT_RADIOBUTTON,changeRed)
#라디오버튼 누르면 changeRed함수 실행
blueRB.Bind(wx.EVT_RADIOBUTTON,changeBlue)
greenRB.Bind(wx.EVT_RADIOBUTTON,changeGreen)

sizer=wx.StaticBoxSizer(wx.VERTICAL,frame,label='배경')
#제목은 '배경'이며 수직적 배치로 틀 만들기
# StaticBoxSizer는 여러 개의 구성 요소 하나로 묶고 제목 지정하고 나열
frame.SetSizer(sizer)
sizer.Add(redRB)
sizer.Add(blueRB)
sizer.Add(greenRB)

frame.Show()
app.MainLoop()
