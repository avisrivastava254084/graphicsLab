import turtle
import time
import math

x1, y1 = eval(input("Enter the coordinates of the first point: "))
x2, y2 = eval(input("Enter the coordinates of the second point: "))

dx = abs(x2-x1)
dy = abs(y2-y1)

if(dx>=dy):
	length = dx
else:
	length = dy

dx = (x2-x1)/length
dy = (y2-y1)/length

x = x1
y = y1

i=1
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
#turtle.write(“One”)

while(i<=length):
	x = x + dx
	y = y + dy
	i = i + 1
	time.sleep(1)
	turtle.goto(x, y)
	turtle.goto(x2, y2)
	#turtle.write(“Two”)
	turtle.penup()
	turtle.hideturtle()
	turtle.done()