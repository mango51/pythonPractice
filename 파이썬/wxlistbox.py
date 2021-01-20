import wx

app=wx.App()
frame=wx.Frame(None)

nameList=['Kim','Lee','Park','Choi','Jeong','Lim','Won','Joo','Yoon']

listBox=wx.ListBox(frame,choices=nameList, style=wx.LB_ALWAYS_SB)

frame.Show()
app.MainLoop()
