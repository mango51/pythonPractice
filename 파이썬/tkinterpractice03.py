from tkinter import *
import tkinter.messagebox

mainFrame = Tk()
mainFrame.geometry('400x400')

Label1 = Label(mainFrame, text='정보 보여주기')
Label1.pack()

def showing():
    tkinter.messagebox.showinfo('이름과 나이','강효민 23')

b1= Button(mainFrame, text='확인', command = showing)
b1.pack()

mainFrame.mainloop()
