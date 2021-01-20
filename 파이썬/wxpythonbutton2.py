import wx

app = wx.App()
frame = wx.Frame(None)

def onClick(event):
    print('Clicked')

btn = wx.Button(frame, label = '클릭')
#frame이라는 프레임에서 '클릭'이라는 버튼 배치
btn.Bind(wx.EVT_BUTTON, onClick)
#btn 버튼에 Bind()함수 적용하여 이벤트 처리할 수 있도록함
#버튼 클릭시 onClick 함수 적용됨

frame.Show()
app.MainLoop()
