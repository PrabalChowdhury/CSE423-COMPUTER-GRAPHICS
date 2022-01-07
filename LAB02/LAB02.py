from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midPoint(x1, y1,x2, y2):
    points = []
    if x1 == x2:
        for i in range(y1, y2 + 1):
            z = (x1, i)
            points.append(z)
        return points
    if y1 == y2:
        for i in range(x1, x2 + 1):
            z = (i, y1)
            points.append(z)
        return points
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        points.reverse()
    return points

def drawid():
    glPointSize(3)
    glBegin(GL_POINTS)
    lst = midPoint(200, 250, 200, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst = midPoint(150, 250, 150, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst1 = midPoint(150, 300, 200, 300)
    i = 0
    while i < len(lst1):
        glVertex2f(lst1[i][0], lst1[i][1])
        i = i + 1
    lst = midPoint(150, 250, 200, 250)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst = midPoint(200, 200, 200, 250)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst = midPoint(150, 200, 150, 250)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst = midPoint(150, 200, 200, 200)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    lst = midPoint(250, 200, 250, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    glEnd()

def iterate():
    glViewport(0, 0, 500, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    drawid()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 400)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID-19101381")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()