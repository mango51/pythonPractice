from tkinter import *
mainFrame = Tk()

sketchbook = Canvas(mainFrame, width = 400, height = 200)
sketchbook.pack()

sketchbook.create_line(10,10,100,100, fill = 'red')
sketchbook.create_rectangle(110,10,200,100, outline= 'black', width='3')
sketchbook.create_oval(210,10,300,100,fill='yellow')

mainFrame.mainloop()
