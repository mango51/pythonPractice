import wx

app = wx.App()
frame = wx.Frame(None, style=wx.MAXIMIZE|wx.CAPTION|wx.CLOSE_BOX, title='제목입니다')

frame.Show()
app.MainLoop()
