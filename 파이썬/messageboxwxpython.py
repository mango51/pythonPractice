import wx
 
app = wx.App()
frame = wx.Frame( None )
 
wx.MessageBox( "안녕하세요", "제목입니다", wx.OK|wx.CANCEL )
#wx.OK 확인버튼, wx.CANCEL 취소버튼
 
frame.Show( True )
app.MainLoop()
