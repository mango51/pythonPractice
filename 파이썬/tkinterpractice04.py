from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame= Tk()

Label1 = Label(mainFrame, text='이름')
Label1.pack()

Label2 = Label(mainFrame, text= '나이')
Label2.pack()

def typing():
    result = tkinter.simpledialog.askstring('이름과 나이 입력하기','이름 입력하기')
    result2 = tkinter.simpledialog.askinteger('이름과 나이 입력하기','나이 입력하기')
    Label1['text'] = result
    Label2['text'] = result2

b1 = Button(mainFrame, text='입력하기',command=typing)
b1.pack()

mainFrame.mainloop()
