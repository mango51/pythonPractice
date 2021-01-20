import turtle as t

def makestamp():
    t.stamp()
    t.ontimer(makestamp, 10000)

def makecircle():
    t.circle(10)
    
def changetogreen():
    t.pencolor('green')

def changetoyellow():
    t.pencolor('yellow')

def changetopink():
    t.pencolor('pink')

def goup(x,y):
    t.clear()

def goingup():
    t.forward(50)

def goingdown():
    t.right(180)

def goingright():
    t.right(90)

def goingleft():
    t.left(90)

t.shape('turtle')
t.onkeypress(makecircle,'c')
t.onkeypress(changetogreen, 'g')
t.onkeypress(changetoyellow,'y')
t.onkeypress(changetopink,'p')
t.onkeypress(goingup, 'Up')
t.onkeypress(goingdown,'Down')
t.onkeypress(goingright,'Right')
t.onkeypress(goingleft,'Left')
t.onscreenclick(goup)
t.ontimer(makestamp, 10000)

t.listen()
t.done()
