from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame= Tk()

Label1 = Label(mainFrame, text='예')
Label1.pack()

Label2 = Label(mainFrame, text='아니오')
Label2.pack()

def selecting():
    result = tkinter.messagebox.askyesno('예 아니오 퀴즈','어렵습니까?')
    if result == True:
        Label1['foreground'] = 'Blue'
    elif result == False:
        Label2['foreground']='Red'

b1 = Button(mainFrame, text='확인하기',command = selecting)
b1.pack()

mainFrame.mainloop()
