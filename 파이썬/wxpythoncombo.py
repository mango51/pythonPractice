import wx

app=wx.App()
frame=wx.Frame(None)

lbl=wx.StaticText(frame,label='과일을 선택 : ')
fruitList=['사과','수박','딸기','오렌지','바나나','키위','오렌지','귤']
combo=wx.ComboBox(frame,choices=fruitList,style=wx.CB_READONLY)

sizer=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(sizer)
sizer.Add(lbl)
sizer.Add(combo)

def changeLabel(event):
    lbl.SetLabelText(combo.GetValue()+'를 선택하셨습니다')

combo.Bind(wx.EVT_COMBOBOX, changeLabel)

frame.Show()
app.MainLoop()
