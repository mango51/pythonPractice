import wx

app=wx.App()
frame=wx.Frame(None)

menubar=wx.MenuBar()
frame.SetMenuBar(menubar)

fileMenu=wx.Menu()
menubar.Append(fileMenu,'파일')
saveItem=wx.MenuItem(id=wx.ID_ANY, text='저장')
openItem=wx.MenuItem(id=wx.ID_ANY,text='열기')
fileMenu.Append(saveItem)
fileMenu.AppendSeparator()
fileMenu.Append(openItem)

def saving(event):
    wx.MessageBox('저장을 눌렀습니다')
frame.Bind(wx.EVT_MENU,saving,saveItem)
#저장 항목 누르면 EVT_MENU 발동하여 saving 함수 작용
#함수 작용하여 '저장을 눌렀습니다' 알림창 뜸

helpMenu=wx.Menu()
menubar.Append(helpMenu,'도움말')
helpItem=wx.MenuItem(id=wx.ID_ANY,text='사용법')
helpMenu.Append(helpItem)

frame.Show()
app.MainLoop()
