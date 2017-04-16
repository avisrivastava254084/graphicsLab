from graphics import *
import time

def moveAll(shapeList, dx, dy):
    for shape in shapeList: 
        shape.move(dx, dy)
            

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)
        

def makeFace(center, win):
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)     # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]

def main():
    win = GraphWin('Back and Forth', 300, 300)
    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    faceList = makeFace(Point(40, 100), win)
    faceList2 = makeFace(Point(150,125), win)

    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):
        moveAllOnLine(faceList, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList, -dx, dy, stepsAcross//2, wait)
        moveAllOnLine(faceList, -dx, -dy, stepsAcross//2, wait)

    win.promptClose(win.getWidth()/2, 20)

main()