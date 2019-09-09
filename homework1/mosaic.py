# Author: Diego Canizales Bollain Goytia
# Matricula: A01376119
# Correo: A01376119@itesm.mx
# Tarea 1: Baldosa

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


w,h= 500,500

def background():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-10, 10)
    glVertex2f(-10, -10)
    glVertex2f(10, -10)
    glVertex2f(10, 10)
    glEnd()

def mosaic():

    colors_to_use = [(1.0, 1.0, 0.0), 
                     (1.0, 0.5, 0.0),
                     (0.0, 0.0, 1.0),
                     (0.0, 0.0, 0.0),
                     (0.0, 0.0, 1.0),
                     (1.0, 0.5, 0.0),
                     (1.0, 1.0, 0.0),
                     (1.0, 1.0, 1.0),
                     (1.0, 1.0, 0.0),
                    ]

    squares_to_draw = [ [(0,15), (15,0), (0,-15), (-15,0)],
                        [(0,13.5), (13.5,0), (0, -13.5), (-13.5,0)],
                        [(0,12), (12,0), (0,-12), (-12,0)],
                        [(0,10.5), (10.5,0), (0,-10.5), (-10.5,0)],
                        [(0,9), (9,0), (0,-9), (-9,0)],
                        [(0,7.5), (7.5,0), (0,-7.5), (-7.5,0)],
                        [(0,6), (6,0), (0,-6), (-6,0)],
                        [(0,4.5), (4.5,0), (0,-4.5), (-4.5,0)],
                        [(0.5, 0), (0,0.5), (-0.5,0), (0,-0.5)]
                    ]

    for i in range (0, len(squares_to_draw)):
        glColor3f(colors_to_use[i][0],colors_to_use[i][1], colors_to_use[i][2])
        glBegin(GL_QUADS)
        square = squares_to_draw[i]
        for vertex in square:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

def triangles():

    triangles_to_draw = [
        [(-0.5, 0.5), (0.5, 0.5), (0, 3)],
        [(-0.5, -0.5), (0.5, -0.5), (0,-3)],
        [(0.5, 0.5), (0.5, -0.5), (3, 0)],
        [(-0.5, 0.5), (-0.5, -0.5), (-3, 0)],
    ]

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    for i in range (0, len(triangles_to_draw)):
        triangle = triangles_to_draw[i]
        for vertex  in triangle:
            glVertex2f(vertex[0], vertex[1])
    glEnd()

def outlines():

    paths_to_draw = [
        [(0,15), (15,0)],
        [(15,0), (0, -15)],
        [(0, -15), (-15, 0)],
        [(-15,0), (0, 15.0)],

        [(0,13.5), (13.5,0)],
        [(13.5,0), (0, -13.5)],
        [(0, -13.5), (-13.5, 0)],
        [(-13.5,0), (0, 13.5)],

        [(0,12), (12,0)],
        [(12,0), (0, -12)],
        [(0, -12), (-12, 0)],
        [(-12,0), (0, 12)],

        [(0,9), (9,0)],
        [(9,0), (0, -9)],
        [(0, -9), (-9, 0)],
        [(-9,0), (0, 9)],

        [(0,7.5), (7.5,0)],
        [(7.5,0), (0, -7.5)],
        [(0, -7.5), (-7.5, 0)],
        [(-7.5,0), (0, 7.5)],

        [(0,6), (6,0)],
        [(6,0), (0, -6)],
        [(0, -6), (-6, 0)],
        [(-6,0), (0, 6)],

        [(0,4.5), (4.5,0)],
        [(4.5,0), (0, -4.5)],
        [(0, -4.5), (-4.5, 0)],
        [(-4.5,0), (0, 4.5)],
        

        [(0, 4.5), (0, 10)],
        [(4.5, 0), (10, 0)],
        [(0, -4.5), (0, -10)],
        [(-4.5,0), (-10,0)]

    ]

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES);
    for i in range(len(paths_to_draw)):
        line = paths_to_draw[i]
        for vertex in line:
            glVertex2f(vertex[0], vertex[1])
    glEnd();


def littleSquares1():
    glBegin(GL_QUADS)
    glVertex2f(-10,2.5)
    glVertex2f(-10,-2.5)
    glVertex2f(-7.5,0)
    glVertex2f(-7.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10,2.5)
    glVertex2f(10,-2.5)
    glVertex2f(7.5,0)
    glVertex2f(7.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-2.5,10)
    glVertex2f(2.5,10)
    glVertex2f(0,7.5)
    glVertex2f(0,7.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-2.5,-10)
    glVertex2f(2.5,-10)
    glVertex2f(0,-7.5)
    glVertex2f(0,-7.5)
    glEnd()

def littleSquares2():
    glBegin(GL_QUADS)
    glVertex2f(-10,2)
    glVertex2f(-10,-2)
    glVertex2f(-8,0)
    glVertex2f(-8,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10,2)
    glVertex2f(10,-2)
    glVertex2f(8,0)
    glVertex2f(8,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-2,10)
    glVertex2f(2,10)
    glVertex2f(0,8)
    glVertex2f(0,8)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-2,-10)
    glVertex2f(2,-10)
    glVertex2f(0,-8)
    glVertex2f(0,-8)
    glEnd()

def littleSquares3():
    glBegin(GL_QUADS)
    glVertex2f(-10,1.5)
    glVertex2f(-10,-1.5)
    glVertex2f(-8.5,0)
    glVertex2f(-8.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10,1.5)
    glVertex2f(10,-1.5)
    glVertex2f(8.5,0)
    glVertex2f(8.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1.5,10)
    glVertex2f(1.5,10)
    glVertex2f(0,8.5)
    glVertex2f(0,8.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1.5,-10)
    glVertex2f(1.5,-10)
    glVertex2f(0,-8.5)
    glVertex2f(0,-8.5)
    glEnd()


def littleSquares4():
    glBegin(GL_QUADS)
    glVertex2f(-10,1)
    glVertex2f(-10,-1)
    glVertex2f(-9,0)
    glVertex2f(-9,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10,1)
    glVertex2f(10,-1)
    glVertex2f(9,0)
    glVertex2f(9,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1,10)
    glVertex2f(1,10)
    glVertex2f(0,9)
    glVertex2f(0,9)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1,-10)
    glVertex2f(1,-10)
    glVertex2f(0,-9)
    glVertex2f(0,-9)
    glEnd()

def littleSquares5():
    glBegin(GL_QUADS)
    glVertex2f(-10,0.5)
    glVertex2f(-10,-0.5)
    glVertex2f(-9.5,0)
    glVertex2f(-9.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10,0.5)
    glVertex2f(10,-0.5)
    glVertex2f(9.5,0)
    glVertex2f(9.5,0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.5,10)
    glVertex2f(0.5,10)
    glVertex2f(0,9.5)
    glVertex2f(0,9.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.5,-10)
    glVertex2f(0.5,-10)
    glVertex2f(0,-9.5)
    glVertex2f(0,-9.5)
    glEnd()

def iterate():
    aspect = float(w)/float(h)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-aspect * 10, aspect * 10, -10, 10, -10, 10)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    background()
    mosaic()
    outlines()

    glColor3f(0.0, 0.0, 0.0)
    littleSquares1()
    glColor3f(1.0, 1.0, 1.0)
    littleSquares2()
    glColor3f(1.0, 0.5, 0.0)
    littleSquares3()
    glColor3f(1.0, 1.0, 0.0)
    littleSquares4()
    glColor3f(0.0, 0.0, 1.0)
    littleSquares5()
    
    triangles()
    glutSwapBuffers()
    



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()