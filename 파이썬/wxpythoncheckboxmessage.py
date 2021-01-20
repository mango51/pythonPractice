import wx

app=wx.App()
frame=wx.Frame(None)

manCheck=wx.CheckBox(frame,label='남자')
womanCheck=wx.CheckBox(frame,label='여자')

def checkMan(event):
    wx.MessageBox('남자를 선택했습니다','당신의 성별은?',wx.OK)

def checkWoman(event):
    wx.MessageBox('여자를 선택했습니다','당신의 성별은?',wx.OK)

manCheck.Bind(wx.EVT_CHECKBOX,checkMan) #체크박스 manCheck 클릭시 checkMan함수 실행
womanCheck.Bind(wx.EVT_CHECKBOX,checkWoman)

sizer=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(sizer)
sizer.Add(manCheck)
sizer.Add(womanCheck) #체크박스 사이저에 수직으로 배치하기

frame.Show()
app.MainLoop()
