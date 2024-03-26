import pygame
import math
from pygame.locals import DOUBLEBUF, OPENGL
from math import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_black_square(size):
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f((- size / 2), (- size / 2))
    glVertex2f((size / 2), (- size / 2))
    glVertex2f((size / 2), (size / 2))
    glVertex2f((- size / 2), (size / 2))
    glEnd()
    
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-50, 50, -50, 50)
    glMatrixMode(GL_MODELVIEW)
    
def animate(value):
    global angle, radius, speed
    angle += speed 
    if (angle >= 360.0):
        angle -= 360.0
    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    pulse_factor = (0.5 * (1 + cos(radians(angle * 4))))
    square_size = 10 + 40 * pulse_factor
    
    glPushMatrix()
    
    glTranslatef(center[0], center[1], 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    draw_black_square(square_size)
    
    glPopMatrix()
    glFlush()
    
pygame.init()
display = (600, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glutInit()

init()

center = (0, 0)
radius = 30
speed = 1.0
angle = 0.0
square_size = 10

glutDisplayFunc(display)
glutTimerFunc(0, animate, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()    