import wx

app=wx.App()
frame=wx.Frame(None)

fruitList=['딸기','사과','수박','복숭아','포도','오렌지','귤','레몬']
basket=[]

fruitBox=wx.ListBox(frame, choices=fruitList)

def buyFruits(event):
    fruit = fruitList[fruitBox.GetSelection()]
    basket.append(fruit)
    print('현재 장바구니 목록 : ', end='')
    for i in basket:
        print(i,end=',')
    print()

fruitBox.Bind(wx.EVT_LISTBOX_DCLICK,buyFruits)

frame.Show()
app.MainLoop()
