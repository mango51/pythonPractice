import wx

app = wx.App()
frame=wx.Frame(None)

btn = wx.Button(frame, label = '클릭')

frame.Show()
app.MainLoop()
