import wx

app = wx.App()
frame=wx.Frame(None)

menubar=wx.MenuBar() #메뉴바 생성
frame.SetMenuBar(menubar) #메뉴바 프레임에 고정

menu1 =wx.Menu() #메뉴 생성
menubar.Append(menu1,'설정') #메뉴바에 설정이라는 메뉴 하나 추가

item1=wx.MenuItem(id=wx.ID_ANY,text='환경설정')
item2=wx.MenuItem(id=wx.ID_ANY,text='종료')
#id=wx.ID_ANY는 아이디 없어도됨이라는 뜻
#메뉴에 쓰일 item들 생성
menu1.Append(item1)
menu1.Append(item2)
#menu1 메뉴에 item1, item2 항목 추가하기

frame.Show()
app.MainLoop()
