from tkinter import *

mainFrame = Tk()
mainFrame.geometry('400x400')
    
sizeLabel = Label(mainFrame, text='크기', font = 'Serif 10')
sizeLabel.pack()


colorLabel = Label(mainFrame, text ='색상', foreground = 'Red')
colorLabel.pack()

def changeSize():
    sizeLabel['font'] = 'Serif 20'


def changeColor():
    colorLabel['foreground']='Blue'

b1 = Button(mainFrame, text='크기 변하기', command=changeSize)
b1.pack()
    
b2= Button(mainFrame, text='색상 변하기',command=changeColor)
b2.pack()

mainFrame.mainloop()
