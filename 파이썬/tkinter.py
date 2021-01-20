from tkinter import *
import tkinter.messagebox

mainFrame = Tk()

tkinter.messagebox.showinfo("몰라", "어쩔")
tkinter.messagebox.showwarning("안녕","hi")
tkinter.messagebox.showerror("제목","메세지")
result = tkinter.messagebox.askyesno("졸리다","졸린가요?")
tkinter.messagebox.askyesnocancel("졸리다","졸린가요?")
tkinter.messagebox.askokcancel("졸리다","졸린가요?")
tkinter.messagebox.askretrycancel("졸리다","졸린가요?")
tkinter.messagebox.askquestion("졸리다","졸린가요?")

if result == True:
    print("예")
elif result == False:
    print("아니요")

mainFrame.mainloop()
