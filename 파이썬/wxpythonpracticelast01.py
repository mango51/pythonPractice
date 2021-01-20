import wx

app = wx.App()
frame=wx.Frame(None)

panel1 = wx.Panel(frame) #패널 생성
panel2 = wx.Panel(frame)

sbsizer1 = wx.StaticBoxSizer(wx.HORIZONTAL, panel1,'성별')
#패널 panel1에 사이저 subsizer1 넣기
sbsizer2=wx.StaticBoxSizer(wx.HORIZONTAL,panel2,'학년')
#패널 panel2에 사이저 subsizer2 넣기
boxsizer=wx.BoxSizer(wx.VERTICAL)

panel1.SetSizer(sbsizer1) #패널에 사이저 위치 고정
panel2.SetSizer(sbsizer2)
frame.SetSizer(boxsizer) #패널에 사이저 위치 고정

gender1= wx.RadioButton(panel1, label='남자',style=wx.RB_GROUP) #라디오버튼 만들기
gender2 = wx.RadioButton(panel1, label='여자')
#style = wx.RB_GROUP을 통해 선택지 중 하나만 고를 수 있도록 함
#다음 wx.RB_GROUP 나올 때까지

sbsizer1.Add(gender1) #패널에 라디오버튼 추가시키기
sbsizer1.Add(gender2)

grade1= wx.RadioButton(panel2, label='1학년', style=wx.RB_GROUP)
grade2=wx.RadioButton(panel2, label='2학년')
grade3 = wx.RadioButton(panel2, label='3학년')

sbsizer2.Add(grade1)
sbsizer2.Add(grade2)
sbsizer2.Add(grade3)

boxsizer.Add(panel1) #sbsizer1 사이저 넣은 패널을 수직적 배치할 사이저 boxsizer 안에 넣기
boxsizer.Add(panel2) #sbsizer2 사이저 넣은 패널을 수직적 배치할 사이저 boxsizer 안에 넣기

frame.Show()
app.MainLoop()
