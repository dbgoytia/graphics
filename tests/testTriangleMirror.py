from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

w,h= 500,500


def triangles():

    a = np.array([[-0.5, 0.5], [0.5, 0.5], [0, 3]])
    reflectionAroudXAxis = np.array([[1, 0], [0, -1]])
    b = a.dot(reflectionAroudXAxis)

    c = np.array([[0.5, 0.5], [0.5, -0.5], [3, 0]])
    reflectionAroundYAxis = np.array([[-1,0], [0, 1]])

    d = c.dot(reflectionAroundYAxis)



    triangles_to_draw = [
        a,
        b,
        c,
        d
    ]

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    for i in range (0, len(triangles_to_draw)):
        triangle = triangles_to_draw[i]
        for vertex  in triangle:
            glVertex2f(vertex[0], vertex[1])
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