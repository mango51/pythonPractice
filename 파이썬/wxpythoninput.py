import wx

app = wx.App()
frame=wx.Frame(None)

inputtxt=wx.TextCtrl(frame)

def changeValue(event):
    line=inputtxt.GetValue()
    frame.SetTitle(line)
    #line에 inputtxt 텍스트 내용 가져오기
    #frame의 title로 line에서 가져온 내용 설정하기

inputtxt.Bind(wx.EVT_TEXT,changeValue)
#텍스트 입력 이벤트 실행시 changeValue함수 실행
#wx.EVT_TEXT 이벤트 상수 = 해당 텍스트 상자의 텍스트가 변경되면 작동하는 이벤트

sizer=wx.BoxSizer(wx.VERTICAL)
#sizer라는 수직 배치되는 박스 설정
frame.SetSizer(sizer)
#sizer를 frame에 설정하기

sizer.Add(inputtxt)

frame.Show()
app.MainLoop()


#텍스트 상자에 입력할 때마다 바로바로 타이틀 내용 즉각적으로 변함
