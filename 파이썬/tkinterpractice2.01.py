from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame=Tk()
mainFrame.geometry('400x800')

menubar = Menu(mainFrame)
mainFrame.config(menu=menubar)

def circle():
    sketchbook = Canvas(mainFrame, width=200, height=200)
    sketchbook.pack()
    sketchbook.create_oval(10,10,190,190,outline='yellow',width='5',fill='pink')

def rectangle():
    sketchbook=Canvas(mainFrame,width=200,height=200)
    sketchbook.pack()
    sketchbook.create_rectangle(10,10,190,190,outline='green')

def line():
    sketchbook=Canvas(mainFrame, width=200, height=200)
    sketchbook.pack()
    sketchbook.create_line(10,10,190,190,fill='purple')
    
item = Menu(menubar)
item2 = Menu(menubar) #메뉴바에 새로운 메뉴 아이템 추가
menubar.add_cascade(label='도형',menu=item)
item.add_command(label='원',command=circle)
item.add_command(label='사각형',command=rectangle)
item.add_command(label='선',command=line)
menubar.add_cascade(label='도움말',menu=item2) #추가된 새로운 메뉴 아이템 이름 지정
item2.add_command(label='정보') #추가된 새로운 메뉴 아이템 하단 항목명 하나 설정
item2.add_command(label='확인')

nameLabel = Label(mainFrame, text='로그인 프로그램',font='Serif 10')
nameLabel.pack()

def login():
    result1= tkinter.simpledialog.askstring('아이디 로그인', '아이디')
    result2 = tkinter.simpledialog.askstring('비밀번호 로그인','비밀번호')

    if result1 == '1' and result2 == 'a':
        print('환영합니다')
    else:
        print('정보가 옳지 않습니다.')

b1 = Button(mainFrame, text='로그인', command=login)
b1.pack()

mainFrame.mainloop()
