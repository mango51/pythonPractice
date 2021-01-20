import wx
 
app = wx.App()
frame = wx.Frame( None )
 
lbl = wx.StaticText( frame, label = "라벨 글씨" )
btn = wx.Button( frame, label = "버튼 글씨" )
 
lbl.SetPosition( wx.Point( 160, 60 ) )
btn.SetPosition( wx.Point( 150, 100 ) )
 
frame.Show()
app.MainLoop()
