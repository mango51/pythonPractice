from tkinter import*

mainFrame = Tk()
mainFrame.geometry('400x200')

nameLabel = Label (mainFrame, text='이름', font = 'Serif 20')
nameLabel.pack()

def changeHong():
    nameLabel['text'] = '홍길동'

hongButton = Button(mainFrame, text= '홍길동으로 변경', command=changeHong)
hongButton.pack()

def changeSeong():
    nameLabel['text'] = '성춘향'

seongButton = Button(mainFrame, text='성춘향으로 변경', command=changeSeong)
seongButton.pack()

mainFrame.mainloop()
