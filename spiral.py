# Write a program to draw a square inside a square?
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,300)
turtle.Screen().title("Spiral patern")
pen=turtle.Turtle()
size=0
while True:
    for i in range(0,4):
        pen.forward(size+1)
        pen.left(90)
        size=size-5
    size=size+1
turtle.done()