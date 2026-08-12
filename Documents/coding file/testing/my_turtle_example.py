
import turtle

pen = turtle.Turtle()   # i got this code from google dang


# Defining a method to draw curve
def curve():
    for i in range(200):

        pen.right(1)
        pen.forward(1)

# Defining method to draw a full heart
def heart():

    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

# Defining method to write text
def txt():
    
    pen.up()
    pen.setpos(-45, 95)
    pen.down()
    pen.color('lightgreen')

    pen.write("I Love You", font=("Verdana", 12, "bold"))

heart()
txt()
pen.ht()

turtle.done()
# This code creates a turtle graphics window and draws an L-shaped figure.
