import wx

app = wx.App()
frame = wx.Frame(None)

def message(event):
    wx.MessageBox('알림창 열기 성공!','제목입니다',wx.OK|wx.CANCEL)

def exiting(event):
    exit(0)
    
lbl1= wx.StaticText(frame, label = '라벨1')
lbl2= wx.StaticText(frame, label='라벨2')
btn1 = wx.Button(frame,label='버튼 누르면 알림창 뜨기')
btn2=wx.Button(frame,label='버튼 누르면 프로그램 종료')

lbl1.SetPosition(wx.Point(160,60))
lbl2.SetPosition(wx.Point(160,100))
btn1.SetPosition(wx.Point(130,140))
btn2.SetPosition(wx.Point(120,180))

btn1.Bind(wx.EVT_BUTTON,message)
btn2.Bind(wx.EVT_BUTTON,exiting)

frame.Show()
app.MainLoop()
