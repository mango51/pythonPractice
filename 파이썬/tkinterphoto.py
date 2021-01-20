from tkinter import *

mainFrame=Tk()
sketchbook = Canvas(mainFrame, width=400, height =600)
sketchbook.pack()

photo = PhotoImage(file='27101-1.png')
sketchbook.create_image(10,10,image=photo, anchor=NW)

mainFrame.mainloop()
