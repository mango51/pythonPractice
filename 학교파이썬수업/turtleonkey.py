import turtle as t

def moveForward():
    t.forward(10)

def turnLeft():
    t.left(90)

def turnRight():
    t.right(90)

def turnBack():
    t.right(180)

t.shape('turtle')
t.onkeypress(moveForward, 'Up')
t.onkeypress(turnLeft, 'Left')
t.onkeypress(turnRight,'Right')
t.onkeypress(turnBack,'Down')

t.listen()
t.done()
