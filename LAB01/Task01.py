from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def drawLines():
    glBegin(GL_LINES)
    glVertex2f(100,150)
    glVertex2f(400,150)
    glVertex2f(100,150)
    glVertex2f(250,450)
    glVertex2f(400,150)
    glVertex2f(250,450)

    glVertex2f(100,350)
    glVertex2f(400,350)
    glVertex2f(100,350)
    glVertex2f(250,50)
    glVertex2f(400,350)
    glVertex2f(250,50)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()




def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    drawLines()
    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()