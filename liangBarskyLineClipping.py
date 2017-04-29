from graphics import *
import time

p = []
q = []

def compute(x1,y1,x2,y2,xwmin,ywmin,xwmax,ywmax):
	point1 = Point(x1,y1)
	points2 = Point(x2,y2)
	dx = x2-x1
	dy = y2-y1
	p.append(-dx)
	q.append(x1-xwmin)
	p.append(dx)
	q.append(xwmax-x1)
	p.append(-dy)
	q.append(y1-ywmin)
	p.append(dy)
	q.append(ywmax-y1)
	
	'''
	for i in range(0,4):
		print (p[i])
	'''
	
	for i in range(0,4):
		if(p[i] == 0):
			print ("Line is parallel to one of the clipping boundary")
			if(q[i] >= 0):
				if(i < 2):
					if(y1 < ywmin):
						y1 = ywmin
					if(y2 > ywmax):
						y2 = ywmax
					line = Line(Point(x1,y1), Point(x2,y2))


	t1 = 0
	t2 = 1
	for i in range(0,4):
		temp = float((q[i])/(p[i]))
		if (p[i] < 0):
			if(t1 <= temp):
				t1 = temp
			elif(t2 > temp):
				t2 = temp

	if(t1<t2):
		xx1 = x1+t1*p[1]
		xx2 = x1+t2*p[1]
		yy1 = y1+t1*p[3]
		yy2 = y1+t2*p[3]
		lineToBeDrawn = Line(Point(xx1,yy1), Point(xx2,yy2))
		win = GraphWin('Back and Forth', 600, 600)
		rect = Rectangle(Point(xwmin,ywmin), Point(xwmax, ywmax))
		rect.draw(win)
		lineToBeDrawn.draw(win)
		win.getMouse()
		
	

compute(120,130,300,310,100,100,250,250)
