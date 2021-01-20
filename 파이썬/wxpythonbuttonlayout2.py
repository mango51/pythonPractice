import wx

app = wx.App()
frame=wx.Frame(None)

btn1 = wx.Button(frame,label='버튼1')
btn2= wx.Button(frame,label='버튼2')
btn3 = wx.Button(frame,label='버튼3')
btn4= wx.Button(frame,label='버튼4')
btn5=wx.Button(frame,label='버튼5')
btn6=wx.Button(frame,label='버튼6')

grid=wx.GridSizer(3,2,10,30)
frame.SetSizer(grid)

grid.Add(btn1,0,wx.EXPAND)
grid.Add(btn2,0,wx.EXPAND)
grid.Add(btn3,0,wx.EXPAND)
grid.Add(btn4,0,wx.EXPAND)
grid.Add(btn5,0,wx.EXPAND)
grid.Add(btn6,0,wx.EXPAND)

frame.Show()
app.MainLoop()
