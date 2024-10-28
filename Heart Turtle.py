import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):

        pen.right(1)
        pen.forward(1)

def heart():

    pen.left(140)
    pen.forward(113)

    curve()
    pen.left(120)

    curve()
    pen.forward(113)

def txt():

    pen.up()
    pen.setpos(-40,95)
    pen.down()

    pen.color("black")

    pen.write("I <3 my boyfriend", font=("Times New Roman", 12))
    
heart()
txt()
pen.ht()
