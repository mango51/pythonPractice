import turtle as t

t.shape('turtle')
t.pendown()
t.pencolor('red')
t.fillcolor('green')
t.begin_fill()
t.circle(50,360,5)
t.end_fill()

t.penup()
t.forward(100)
t.pendown()

t.pencolor('blue')
t.fillcolor('pink')
t.begin_fill()
t.circle(50,360,6)
t.end_fill()

t.penup()
t.forward(100)
t.pendown()

t.pencolor('yellow')
t.fillcolor('orange')
t.begin_fill()
t.circle(50,360,7)
t.end_fill()
