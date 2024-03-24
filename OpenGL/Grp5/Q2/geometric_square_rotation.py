from math import cos, pi, sin
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# function to drawing the black square
def draw_black_square(x, y, size):
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(((x - size) / 2), ((y - size) / 2))
    glVertex2f(((x + size) / 2), ((y - size) / 2))
    glVertex2f(((x + size) / 2), ((y + size) / 2))
    glVertex2f(((x - size) / 2), ((y + size) / 2))
    glEnd()
    
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
    
    newX = center[0] + (radius * cos(angle * (pi / 180.0)))
    newY = center[0] + (radius * sin(angle * (pi / 180.0)))
    
    glTranslatef(newX, newY, 0)
    # rotate clockwise about the square center
    glRotatef(-angle, 0.0, 0.0, 1.0)
    draw_black_square(0, 0, square_size)
    

pygame.init()
display = (900, 900)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


glClearColor(1.0, 1.0, 1.0, 1.0)
gluOrtho2D(-50, 50, -50, 50)

center = (0, 0)
radius = 30
speed = 3.0     #adjust the speed for one revolution per quarter path
angle = 0.0
sqaure_size = 10

glutDisplayFunc(display)
glutTimerFunc(0, animate, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()