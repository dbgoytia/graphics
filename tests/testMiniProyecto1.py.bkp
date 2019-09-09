# Autor: Diego Canizales Bollain Goytia
# Matricula: A01376119
# Fecha: Septiembre 8 de 2019
# Graficas Computacionales
# Profesor Wilmer Pereira
# 
# Mini proyecto del primer parcial

# Imports for using PyOpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


w,h = 1240,960          # Global values for viewports
rotate_by_key = 0       # Global rotation value 
pivot_x = 0
pivot_y = 0
scale = 1

def draw_tile():
    
    # Rotation for the given tile, updated by global value of rotate_by_key
    # and using OPENGL matrix manipulation facilities (glRotatef, glTranslatef)
    # Scaling for the given tile is updated by global value of scale,
    # and using OPENGL matrix manipulation facilities (glScalef)
    global rotate_by_key, pivot_x, pivot_y, scale


    # Finish if the center of the object exits the viewport (works even when scaled)
    if pivot_x > 30 and pivot_y > 30:
        # Exit if it touches upper right corner
        glutLeaveMainLoop()
    elif scale > 10:
        # Exit if scale gets too big
        glutLeaveMainLoop()
    elif pivot_x < -30 and pivot_y < -30:
        # Exit if it touches lower left corner
        glutLeaveMainLoop
    elif scale <= 0.001:
        # Exit if scale gets too small
        glutLeaveMainLoop()
    

    glTranslatef(pivot_x, pivot_y, 0) # First, move the element to origin, then rotate.
    glRotatef(rotate_by_key, 0, 0, 1)
    #glTranslatef(-pivot_x, -pivot_y, 0)
    glScalef(scale, scale, scale)


    # Array of colors to paing the tile
    colors_to_use = [
                    (0.0, 1.0, 1.0), 
                    (1.0, 1.0, 0.0), 
                    (1.0, 0.5, 0.0),
                    (0.0, 0.0, 1.0),
                    (1.0, 1.0, 0.0),
                    (0.0, 1.0, 0.0),
                    (0.0, 0.0, 1.0),
                    (1.0, 1.0, 0.0),
                    (0.0, 1.0, 0.0),
                    (0.0, 1.0, 1.0), 
                    (1.0, 1.0, 0.0), 
                    (1.0, 0.5, 0.0),
                    ]

    # Array of squares to draw
    squares_to_draw = [ 
                        [(16.5,16.5), (-16.5,16.5), (-16.5,-16.5), (16.5,-16.5)],
                        [(15.5,15.5), (-15.5,15.5), (-15.5,-15.5), (15.5,-15.5)],
                        [(13, 13), (-13,13), (-13,-13), (13,-13)],
                        [(10.5,10.5), (-10.5,10.5), (-10.5,-10.5), (10.5,-10.5)],
                        [(0,16.5), (16.5,0), (0,-16.5), (-16.5,0)],
                        [(0,13), (13,0), (0,-13), (-13,0)],
                        [(0,11.5), (11.5,0), (0,-11.5), (-11.5,0)],
                        [(0,9.5), (9.5,0), (0,-9.5), (-9.5,0)],
                        [(0,7.5), (7.5,0), (0,-7.5), (-7.5,0)],
                        [(0,5.5), (5.5,0), (0,-5.5), (-5.5,0)],
                        [(0,3.5), (3.5,0), (0,-3.5), (-3.5,0)],
                        [(0,1.5), (1.5,0), (0,-1.5), (-1.5,0)],
                    ]

    # Function to iterate over the array of squares, assign them a color, and paint them on viewport
    for i in range (0, len(squares_to_draw)):
        glColor3f(colors_to_use[i][0],colors_to_use[i][1], colors_to_use[i][2]) # Assign a color
        glBegin(GL_QUADS)  # Draw quads directive
        square = squares_to_draw[i] # The square that we're currently going to paint on viewport.
        for vertex in square: # Paint all vertexes on viewport
            glVertex2f(vertex[0], vertex[1])
        glEnd()

def iterate():
    # Iterate over the viewport for correct projection of image
    aspect = float(w)/float(h)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-aspect * 30, aspect * 30, -30, 30, -30, 30)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def render():
    # Render images
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the screen and the buffer
    glLoadIdentity() # Reset the view
    iterate()
    draw_tile() # Draws the tile
    glutSwapBuffers() # Swap buffers at the end because we're using multiple buffers


# Keyboard input handler
def keyboard(key, x, y):
    global rotate_by_key, pivot_x, pivot_y, scale

    # Exits the program if capital 'F' is pressed
    if ord(key) == 70: # ord() is needed to get the keycode
        glutLeaveMainLoop()
        return 

    # Counter clockwise rotation: activated with lowercase 'r'
    if ord(key) == 114:# lowercase 'r'
        rotate_by_key += 10 
        print("rotate! :" + str(rotate_by_key))
        return

    # Clockwise rotation: activated with lowercase 'u'
    if ord(key) == 117:# lowercase 'u'
        rotate_by_key -= 10 
        return

    # Translate in both x and y 10 positions using capital "T"
    if ord(key) == 84:
        glPushMatrix() # Generate a new layer
        pivot_x += 10
        pivot_y += 10
        glTranslatef(pivot_x, pivot_y, 0.0)
        print("x: " +str(pivot_x))
        print("y:" + str(pivot_y))
        draw_tile()
        glPopMatrix()
        return
    
    # Translate in both x and y -10 position using lowercase "t"
    if ord(key) == 116:
        glPushMatrix() # Generate a new layer
        pivot_x -= 10
        pivot_y -= 10
        glTranslatef(pivot_x, pivot_y, 0.0)
        print("x: " +str(pivot_x))
        print("y:" + str(pivot_y))
        draw_tile()
        glPopMatrix()
        return

    # Scale the image (bigger)
    if ord(key) == 69:
        if scale <= 1:
            scale = scale *2
        else:
            scale = scale + 1
        return
    
    # Scale the image (smaller)
    if ord(key) == 101:
        print(scale)
        if scale <= 1:
            scale = scale/2
        else:
            scale -= 1
        return



def main():
    glutInit() # Initialize glut window manager
    glutInitDisplayMode(GLUT_RGBA) 
    glutInitWindowSize(1240, 960) # Window size
    glutInitWindowPosition(0, 0) # starting position for drawing
    glutCreateWindow("OpenGL Coding Practice") # Title
    glutDisplayFunc(render) # Render tile
    glutIdleFunc(render) # Render tile
    glutKeyboardFunc(keyboard) # Get input from user to manipulate tile
    glutMainLoop()

if __name__ == '__main__':
    main()