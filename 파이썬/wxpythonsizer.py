import wx

app=wx.App()
frame=wx.Frame(None)

idtxt=wx.TextCtrl(frame,value='아이디')
pwtxt=wx.TextCtrl(frame,value='비밀번호',style=wx.TE_PASSWORD)
#입력한 값 감춰져서 보임

sizer=wx.BoxSizer(wx.VERTICAL) #수직으로 배치하도록 틀 만듬
frame.SetSizer(sizer) #만든 틀 frame에 적용하기
sizer.Add(idtxt) #텍스트박스 틀 안에 넣기
sizer.Add(pwtxt)

frame.Show()
app.MainLoop()
