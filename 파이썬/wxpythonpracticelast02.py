import wx

app=wx.App()
frame=wx.Frame(None)

panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)
panel3 = wx.Panel(frame)
panel4 = wx.Panel(frame)


sizer1 = wx.BoxSizer(wx.VERTICAL)
panel1.SetSizer(sizer1) #패널 panel1에 sizer1 고정 (배치)

label1 = wx.StaticText(panel1, label='이름') #패널 panel1에 텍스트 생성
text1 = wx.TextCtrl(panel1) #패널 panel1에 input 생성
sizer1.Add(label1) #panel1에 있는 사이저 sizer1에 텍스트 추가
sizer1.Add(text1)


sizer2= wx.StaticBoxSizer(wx.VERTICAL, panel2, '성별')
panel2.SetSizer(sizer2)

radio1 = wx.RadioButton(panel2, label='남', style=wx.RB_GROUP)
radio2 = wx.RadioButton(panel2, label='여')
sizer2.Add(radio1)
sizer2.Add(radio2)


sizer3= wx.StaticBoxSizer(wx.VERTICAL, panel3, '취미')
panel3.SetSizer(sizer3)

check1 = wx.CheckBox(panel3, label='영화')
check2 = wx.CheckBox(panel3, label='독서')
check3 = wx.CheckBox(panel3, label='여행')
check4 = wx.CheckBox(panel3, label='운동')
sizer3.Add(check1)
sizer3.Add(check2)
sizer3.Add(check3)
sizer3.Add(check4)


sizer4 = wx.BoxSizer(wx.VERTICAL)
# panel4.SetSizer(sizer4) 해도 상관 없음
# 마지막으로 남은 사이저라 안해도됨 (자동배치)

button1 = wx.Button(panel4,label='입력')
sizer4.Add(button1, flag=wx.ALIGN_CENTER)
#flag = wx.ALIGN_CENTER로 가운데 배치

sizer5= wx.GridSizer(2,2,10,10)
#wx.GridSizer(가로 줄 수, 세로 줄 수, 상하 여백, 좌우 여백)
frame.SetSizer(sizer5) #그리드 사이저를 프레임에 설정/배치
sizer5.Add(panel1,0,wx.EXPAND) 
sizer5.Add(panel2,0,wx.EXPAND)
sizer5.Add(panel3,0,wx.EXPAND)
sizer5.Add(panel4,0,wx.EXPAND)
#Add(구성요소, 번호, 속성)
#Add(추가할 대상, 0, wx.EXPAND)
#wx.EXPAND = 가득 채우기

frame.Show()
app.MainLoop()
