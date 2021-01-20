import wx
 
app = wx.App()
frame = wx.Frame( None )
 
lbl = wx.StaticText( frame, label = "라벨 글씨" )
btn = wx.Button( frame, label = "버튼 글씨" )
 
frame.Show()
app.MainLoop()
