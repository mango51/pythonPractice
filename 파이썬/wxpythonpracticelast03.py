import wx

app = wx.App()
frame= wx.Frame(None)

panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)
panel3 = wx.Panel(frame)
panel4 = wx.Panel(frame)

sizer1 = wx.BoxSizer(wx.HORIZONTAL)
panel1.SetSizer(sizer1)
label1= wx.StaticText(frame, label='성적 입력 시스템')
sizer1.Add(label1)

sizer2= wx.StaticBoxSizer(wx.HORIZONTAL, panel2, label='국어')
panel2.SetSizer(sizer2)
text1= wx.TextCtrl(panel2)
#wx.TextCtrl(input 텍스트를 넣을 프레임)
sizer2.Add(text1) #패널 안에 있는 텍스트 사이저에 추가

sizer3 = wx.StaticBoxSizer(wx.HORIZONTAL, panel3, label='수학')
panel3.SetSizer(sizer3) #panel3에 sizer3 고정시키기
text2 = wx.TextCtrl(panel3) #panel3에 text2 생성
sizer3.Add(text2) #panel3에 생성한 text2를 sizer3 사이저에 추가하기

sizer4 = wx.StaticBoxSizer(wx.HORIZONTAL, panel4, label='영어')
panel4.SetSizer(sizer4)
grade=['A','B','C','D']
combo1=wx.ComboBox(panel4,choices=grade, style=wx.CB_READONLY)
#수정 안되도록 style = wx.CB_READONLY
sizer4.Add(combo1)

sizer5=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(sizer5) #프레임에 사이저 sizer5 고정시키기
sizer5.Add(panel1)
sizer5.Add(panel2)
sizer5.Add(panel3)
sizer5.Add(panel4)

frame.Show()
app.MainLoop()
