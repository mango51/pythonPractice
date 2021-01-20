from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()

result = tkinter.simpledialog.askinteger("제목", "나이")
print(result)

mainFrame.mainloop()
