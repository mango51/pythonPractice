import wx

app=wx.App()
frame=wx.Frame(None)

menubar=wx.MenuBar()
frame.SetMenuBar(menubar)

menu1=wx.Menu()
menubar.Append(menu1,'파일')

menu2=wx.Menu()
menubar.Append(menu2,'설정')

menu3=wx.Menu()
menubar.Append(menu3,'도움말')

frame.Show()
app.MainLoop()
