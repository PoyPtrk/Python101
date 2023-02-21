import turtle

t = turtle
t.Pen()
t.shape('turtle')

t.left(60)
t.pensize(5)
colors =["black","red","green","black","blue","green"]

for i in range (6):
    t.pencolor(colors[i])
    t.forward(60)
    t.left(60)
    t.forward(60)
    t.left(60)
    t.forward(10)
    t.left(120)
    t.forward(60)
    t.right(60)
    t.forward(60)
    t.right(60)

    t.penup()
    t.forward(70)
    t.right(180)

    t.pendown()



