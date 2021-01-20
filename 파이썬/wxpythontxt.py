import wx

app=wx.App()
frame=wx.Frame(None)

inputtxt=wx.TextCtrl(frame)
outputtxt=wx.TextCtrl(frame,style=wx.TE_READONLY,value='주목해주세요')
#수정할 수 없는 outputtxt (바뀌기 전, 디폴트 값 = '주목하세요')

def changeValue(event):
    line=inputtxt.GetValue()    #inputtxt에 적힌 텍스트 가져와서 line변수에 대입
    outputtxt.SetValue(line)    #outputtxt에 line이 가지고  있는 텍스트 설정하기
    #line에 있는 내용 outputtxt로 가져와서 붙이기

btn=wx.Button(frame,label='변경')
btn.Bind(wx.EVT_BUTTON,changeValue) #버튼 누르면 changeValue 함수 실행

sizer=wx.BoxSizer(wx.VERTICAL) #수직으로 배치 틀 만들기
frame.SetSizer(sizer)

sizer.Add(inputtxt) 
sizer.Add(outputtxt)
sizer.Add(btn)

frame.Show()
app.MainLoop()
