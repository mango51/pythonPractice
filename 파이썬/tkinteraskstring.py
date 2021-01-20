from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()

result = tkinter.simpledialog.askstring("이름", "이름 입력하기")
print(result)

mainFrame.mainloop()
