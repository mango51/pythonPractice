import wx

app=wx.App()
frame=wx.Frame(None)

frame.SetTitle('제목 미정')
mainSizer=wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(mainSizer) #사이저 프레임에 고정

numbers=[]
expression=[]

#계산기 함수들에 대한 부분
def number1(event):
    line=numberFld.GetValue()
    line=line+'1'
    numberFld.SetValue(line)

def number2(event):
    line=numberFld.GetValue()
    line=line+'2'
    numberFld.SetValue(line)

def number3(event):
    line=numberFld.GetValue()
    line=line+'3'
    numberFld.SetValue(line)

def number4(event):
    line=numberFld.GetValue()
    line=line+'4'
    numberFld.SetValue(line)

def number5(event):
    line=numberFld.GetValue()
    line=line+'5'
    numberFld.SetValue(line)

def number6(event):
    line=numberFld.GetValue()
    line=line+'6'
    numberFld.SetValue(line)

def number7(event):
    line=numberFld.GetValue()
    line=line+'7'
    numberFld.SetValue(line)

def number8(event):
    line=numberFld.GetValue()
    line=line+'8'
    numberFld.SetValue(line)

def number9(event):
    line=numberFld.GetValue()
    line=line+'9'
    numberFld.SetValue(line)

def number00(event):
    line=numberFld.GetValue()
    line=line+'00'
    numberFld.SetValue(line)

def number0(event):
    line=numberFld.GetValue()
    line=line+'0'
    numberFld.SetValue(line)

def addEquals(event):
    line=numberFld.GetValue()
    numbers.append(int(line))

    print("result : ", expression[0])

    if expression[0] == '+':
        numberFld.SetValue(str(numbers[0] + numbers[1]))
    elif expression[0]=='-':
        numberFld.SetValue(str(numbers[0] - numbers[1]))
    elif expression[0]=='*':
        numberFld.SetValue(str(numbers[0] * numbers[1]))
    elif expression[0]=='/':
        numberFld.SetValue(str(numbers[0] / numbers[1]))
    else:
        numberFld.SetValue(str(numbers[0]))

def addPlus(event):
    line=numberFld.GetValue()
    numbers.append(int(line))
    expression.append('+')
    line=''
    numberFld.SetValue(line)

def addMinus(event):
    line=numberFld.GetValue()
    numbers.append(int(line))
    expression.append('-')
    line=''
    numberFld.SetValue(line)

def addMultiple(event):
    line=numberFld.GetValue()
    numbers.append(int(line))
    expression.append('*')
    line=''
    numberFd.SetValue(line)

def addDivision(event):
    line=numberFld.GetValue()
    numbers.append(int(line))
    expression.append('/')
    line=''
    numberFld.SetValue(line)

menubar=wx.MenuBar()
frame.SetMenuBar(menubar)

def setTitle(event):
    frame.SetTitle('제목 변경 완료')

def resetTitle(event):
    frame.SetTitle('제목 미정')

setMenu=wx.Menu()
titleItem=wx.MenuItem(id=wx.ID_ANY, text='제목 변경')
resetItem=wx.MenuItem(id=wx.ID_ANY, text='제목 초기화')
menubar.Append(setMenu,'설정')
setMenu.Append(titleItem)
setMenu.AppendSeparator()
setMenu.Append(resetItem)

setMenu.Bind(wx.EVT_MENU, setTitle, titleItem)
setMenu.Bind(wx.EVT_MENU, resetTitle, resetItem)
#해당 프레임.Bind(wx.EVT_MENU, 함수이름, 메뉴 아이템 이름)

#숫자를 보여주는 부분
panel1= wx.Panel(frame)
p1Sizer=wx.GridSizer(1,1,50,50)
panel1.SetSizer(p1Sizer)

numberFld=wx.TextCtrl(panel1, style=wx.TE_READONLY)

p1Sizer.Add(numberFld, flag=wx.EXPAND)

mainSizer.Add(panel1, flag=wx.EXPAND)

#키패드를 담는 부분
panel2 = wx.Panel(frame)
p2Sizer=wx.BoxSizer(wx.HORIZONTAL)
panel2.SetSizer(p2Sizer)

mainSizer.Add(panel2, flag=wx.EXPAND)

#숫자들을 보여주는 부분
panel3=wx.Panel(panel2)
p3Sizer=wx.GridSizer(4,3,10,10)
panel3.SetSizer(p3Sizer)

btn1=wx.Button(panel3, label='1')
btn2=wx.Button(panel3, label='2')
btn3=wx.Button(panel3, label='3')
btn4=wx.Button(panel3, label='4')
btn5=wx.Button(panel3, label='5')
btn6=wx.Button(panel3, label='6')
btn7=wx.Button(panel3, label='7')
btn8=wx.Button(panel3, label='8')
btn9=wx.Button(panel3, label='9')
btn0=wx.Button(panel3, label='00')
btn00=wx.Button(panel3, label='0')
equalsBtn=wx.Button(panel3, label='=')

btn1.Bind(wx.EVT_BUTTON, number1)
btn2.Bind(wx.EVT_BUTTON, number2)
btn3.Bind(wx.EVT_BUTTON, number3)
btn4.Bind(wx.EVT_BUTTON, number4)
btn5.Bind(wx.EVT_BUTTON, number5)
btn6.Bind(wx.EVT_BUTTON, number6)
btn7.Bind(wx.EVT_BUTTON, number7)
btn8.Bind(wx.EVT_BUTTON, number8)
btn9.Bind(wx.EVT_BUTTON, number9)
btn00.Bind(wx.EVT_BUTTON, number00)
btn0.Bind(wx.EVT_BUTTON, number0)
equalsBtn.Bind(wx.EVT_BUTTON, addEquals)

p3Sizer.Add(btn1)
p3Sizer.Add(btn2)
p3Sizer.Add(btn3)
p3Sizer.Add(btn4)
p3Sizer.Add(btn5)
p3Sizer.Add(btn6)
p3Sizer.Add(btn7)
p3Sizer.Add(btn8)
p3Sizer.Add(btn9)
p3Sizer.Add(btn00)
p3Sizer.Add(btn0)
p3Sizer.Add(equalsBtn)

p2Sizer.Add(panel3, flag=wx.EXPAND)

#연산 기호를 보여주는 부분
panel4 = wx.Panel(panel2)
p4Sizer=wx.GridSizer(4,1,10,10)
panel4.SetSizer(p4Sizer)

plusBtn=wx.Button(panel4,label='+')
minusBtn=wx.Button(panel4, label='-')
multipleBtn=wx.Button(panel4, label='*')
divisionBtn=wx.Button(panel4, label='/')

plusBtn.Bind(wx.EVT_BUTTON, addPlus)
minusBtn.Bind(wx.EVT_BUTTON, addMinus)
multipleBtn.Bind(wx.EVT_BUTTON,addMultiple)
divisionBtn.Bind(wx.EVT_BUTTON,addDivision)

p4Sizer.Add(plusBtn, flag=wx.EXPAND)
p4Sizer.Add(minusBtn, flag=wx.EXPAND)
p4Sizer.Add(multipleBtn, flag=wx.EXPAND)
p4Sizer.Add(divisionBtn, flag=wx.EXPAND)

p2Sizer.Add(panel4, flag=wx.EXPAND)

frame.Show()
app.MainLoop()
