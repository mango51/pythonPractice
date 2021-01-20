from tkinter import*
mainFrame = Tk()

mainFrame.title('파이썬 그래픽 테스트')
mainFrame.geometry('400x200')
appleButton = Button(mainFrame, text='사과', foreground = 'Red')
appleButton.pack()
mainFrame.mainloop()
