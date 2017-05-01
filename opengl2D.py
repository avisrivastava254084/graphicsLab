from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos

g_Width = 400
g_Height = 400

ballXCoord = 0.0
ballYCoord = 0.0
ballRadius = 0.04
xAxisSpeed = 0.04
yAxisSpeed = 0.009

def scenemodel():
    global ballXCoord, ballYCoord, ballRadius, xAxisSpeed, yAxisSpeed
    
    print ballXCoord, ballYCoord
    
    glTranslatef(ballXCoord, ballYCoord, 0.0);
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.0)
    
    numSegments = 2000

    for i in range(numSegments):
        angle = i*2.0*pi/numSegments
        glVertex2f(cos(angle) * ballRadius, sin(angle) * ballRadius)

    glEnd()

    if ballXCoord < 1:
        ballXCoord += xAxisSpeed
        ballYCoord += yAxisSpeed
    else:
        ballXCoord = -ballXCoord
        ballYCoord = -ballYCoord


    glutPostRedisplay()


def resetView():
    glutPostRedisplay()

def display():
    # Clear frame buffer
    glClear(GL_COLOR_BUFFER_BIT)
    # Set up viewing transformation, looking down -Z axis
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    # Rendering the scene
    scenemodel()
    # To make sure changes appear onscreen
    glutSwapBuffers()


def reshape(width, height):
    global g_Width, g_Height
    g_Width = width
    g_Height = height
    glViewport(0, 0, g_Width, g_Height)
    
  

def keyboard(key, x, y):
    global zTr, yTr, xTr
    if(key=='r'): resetView()
    if(key=='q'): exit(0)
    glutPostRedisplay()



if __name__=="__main__":
    # GLUT Window Initialization
    glutInit()
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)      # zBuffer
    glutInitWindowSize (g_Width,g_Height) 
    glutInitWindowPosition (0 + 4, g_Height / 4)
    glutCreateWindow ("Graphics Lab OpenGL")
    
    # Register callbacks
    glutReshapeFunc(reshape)
    for i in range(1000):
        glutDisplayFunc(display)    
    
    glutKeyboardFunc(keyboard)
    # Turn the flow of control over to GLUT
    glutMainLoop()
