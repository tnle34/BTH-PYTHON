import turtle, random
colors = ['red','gold','green','blue','orange','purple','pink','yellow','black']
painter=turtle.Turtle()
painter.pensize(5)
for i in range (12):
    color=random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)
