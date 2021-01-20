import wx

app = wx.App()
frame = wx.Frame(None)

def clicking(event):
    print('클릭됨')
    

btn = wx.Button(frame, label='클릭')
#wx모듈에서 Button이라는 기능 사용
btn.Bind(wx.EVT_BUTTON, clicking)

lbl = wx.StaticText(frame, label='라벨입니다')
#wx모듈에서 StaticText로 라벨 만들기

frame.Show()
app.MainLoop()
