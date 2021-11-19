from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


"""def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
"""
"""def drawLines():
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
    glEnd()"""
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def DDA(x1, x2, y1, y2):
    glPointSize(5)
    """m = (y1-y2)/(x1-x2)"""
    if y1 == y2:
        glBegin(GL_POINTS)
        while x1 < x2:
            x1 = x1 + 1
            glVertex2f(x1, round(y1))
        glEnd()
    elif x1 == x2:
        glBegin(GL_POINTS)
        while y1 < y2:
            y1 = y1 + 1
            glVertex2f(x1, y1)
        glEnd()
    else:
        m = (y2 - y1) / (x2 - x1)
        if -1 < m and m > 1:
            glBegin(GL_POINTS)
            while x1 < x2:
                x1 = x1 + 1
                y1 = y1 + m
                glVertex2f(x1, round(y1))
            glEnd()
        else:
            glBegin(GL_POINTS)
            while y1 < y2:
                x1 = x1 + m
                y1 = y1 + 1
                glVertex2f(round(x1), y1)
            glEnd()
def DDA_Dot(x1, x2, y1, y2):
    glPointSize(2)
    # m = (y1-y2)/(x1-x2)
    u = 0
    if y1 == y2:
        glBegin(GL_POINTS)
        while x1 < x2:
            x1 = x1 + 1
            if u%2==0:
                glVertex2f(x1, round(y1))
            u = u + 1
        glEnd()
    elif x1 == x2:
        glBegin(GL_POINTS)
        while y1 < y2:
            y1 = y1 + 1
            if u % 4 ==0:
                glVertex2f(x1, round(y1))
            u = u + 1
        glEnd()
    else:
        m = (y2 - y1) / (x2 - x1)
        if -1 < m and m > 1:
            glBegin(GL_POINTS)
            while x1 < x2:
                x1 = x1 + 1
                y1 = y1 + m
                if u % 2==0:
                    glVertex2f(x1, round(y1))
                u = u + 1
            glEnd()
        else:
            glBegin(GL_POINTS)
            while y1 < y2:
                x1 = x1 + m
                y1 = y1 + 1
                if u % 2 == 0:
                    glVertex2f(round(x1), y1)
                u = u + 1
            glEnd()
def Even():
    DDA_Dot(100,400,250,250)
    DDA(100,100,100,400)
    DDA(100,400,100,100)
    DDA(100,400,400,400)
def Odd():
    DDA_Dot(100,280,250,250)
    DDA(100,100,100,400)
    DDA(100,400,400,400)
def Id(a):
    if a%2==0:
        Even()
    else:
        Odd()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here  
    Id(19101381)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1500, 1500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()