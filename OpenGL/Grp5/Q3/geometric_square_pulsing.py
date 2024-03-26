from turtle import speed
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_black_square(x, y, size):
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(((x - size) / 2), ((y - size) / 2))
    glVertex2f(((x + size) / 2), ((y - size) / 2))
    glVertex2f(((x + size) / 2), ((y + size) / 2))
    glVertex2f(((x - size) / 2), ((y + size) / 2))
    glEnd()
    
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-50, 50, -50, 50)
    glMatrixMode(GL_MODELVIEW)
    
def animate(value):
    global angle, radius, speed, pulse_cycle, pulse_direction, square_size
    angle += speed
    
    # check if a full revolution is completed
    if (angle >= 360.0):
        angle -= 360.0
        pulse_cycle += 1
        
        
        # reverse the pulse direction at the end of each cycle
        if (pulse_direction == 1):
            pulse_direction -= 1
        else:
            pulse_direction = 1
            
        # calculate the pulse effect
        pulse_factor = (0.5 * (1 + pulse_direction * (1 - (angle % 90) / 90)))
        square_size = 10 * pulse_factor
        
        glutPostRedisplay()
        glutTimerFunc(30, animate, 0)
        
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    glTranslatef(center[0], center[1], 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glTranslatef(radius, 0.0, 0.0)
    
    draw_black_square(square_size)
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