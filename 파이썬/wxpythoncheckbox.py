import wx

app=wx.App()
frame=wx.Frame(None)

manCheck=wx.CheckBox(frame, label='남자')
womanCheck=wx.CheckBox(frame, label='여자')

sizer=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(sizer)
sizer.Add(manCheck)
sizer.Add(womanCheck)

frame.Show()
app.MainLoop()
