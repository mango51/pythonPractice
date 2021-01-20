import wx

app=wx.App()
frame=wx.Frame(None)

redRB=wx.RadioButton(frame,label='빨강',style=wx.RB_GROUP)
blueRB=wx.RadioButton(frame,label='파랑')
greenRB=wx.RadioButton(frame,label='초록')
#여기 세 가지 선택지 중 하나만 선택 가능

circleRB = wx.RadioButton(frame, label='원형', style=wx.RB_GROUP)
rectangleRB=wx.RadioButton(frame,label='사각형')
triangleRB=wx.RadioButton(frame,label='삼각형')
#여기 세 가지 선택지 중 하나만 선택 가능


#이와 같이 style에 RB_GROUP을 써준 버튼을 기준으로 두 개의 묶음이 생긴 것 확인 가능

sizer=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(sizer)
sizer.Add(redRB)
sizer.Add(blueRB)
sizer.Add(greenRB) #3가지 선택지 중 하나만 선택 가능

sizer.Add(circleRB)
sizer.Add(rectangleRB)
sizer.Add(triangleRB) #3가지 선택지 중 하나만 선택 가능

frame.Show()
app.MainLoop()
