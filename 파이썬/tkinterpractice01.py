from tkinter import *

mainFrame = Tk()
mainFrame.geometry('400x400')

quizLabel = Label(mainFrame, text = '위치', font = 'Serif 20')
quizLabel.pack()

def changeLeft():
    quizLabel['text'] = '왼쪽'
    
def changeRight():
    quizLabel['text'] = '오른쪽'

b1 = Button(mainFrame, text = '왼쪽', command = changeLeft)
b1.pack(side = 'left')

b2 = Button(mainFrame, text = '오른쪽', command = changeRight)
b2.pack(side='right')


mainFrame.mainloop()
