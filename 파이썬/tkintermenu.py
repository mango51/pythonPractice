from tkinter import *

mainFrame= Tk()
mainFrame.geometry('400x200')

menubar = Menu(mainFrame)
mainFrame.config(menu = menubar)

item=Menu(menubar)
menubar.add_cascade(label='파일', menu=item)

def save():
    print('저장 버튼')

item.add_command(label='저장',command=save)

mainFrame.mainloop()
