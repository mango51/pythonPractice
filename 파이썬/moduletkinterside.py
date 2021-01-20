from tkinter import *

mainFrame = Tk()
mainFrame.geometry('500x500')

b1 = Button(mainFrame, text='1')
b1.pack(side = 'right')
b2 = Button(mainFrame, text='2')
b2.pack(side='right')
b3 = Button(mainFrame, text='3')
b3.pack(side='left')
b4 = Button(mainFrame, text='4')
b4.pack()


mainFrame.mainloop()
