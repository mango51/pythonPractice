import wx

app = wx.App()
frame = wx.Frame(None)

btn = wx.Button(frame, label='1')
btn1 = wx.Button(frame, label='2')
btn2=wx.Button(frame, label='3')

box=wx.StaticBoxSizer(wx.HORIZONTAL,frame,'버튼 목록')
frame.SetSizer(box)
box.Add(btn)
box.Add(btn1,flag=wx.ALIGN_CENTER)
box.Add(btn2,flag=wx.ALIGN_BOTTOM)

frame.Show()
app.MainLoop()
