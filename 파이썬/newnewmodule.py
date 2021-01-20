import wx

app = wx.App()
frame = wx.Frame(None,pos=(0 ,0),style=wx.MAXIMIZE|wx.CAPTION|wx.CLOSE_BOX)

frame.Show(True)
app.MainLoop()
