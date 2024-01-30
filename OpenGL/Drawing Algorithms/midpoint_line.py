import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_pixel(x, y):
    glColor(1, 1, 1)
    glVertex2f(x, y)


def draw_line_midpoint(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    # Initial decision parameter for the midpoint algorithm
    d = dy - (dx / 2)

    # Initial coordinates
    x, y = x0, y0

    # Plot the first pixel
    draw_pixel(x, y)

    # Main loop
    for i in range(dx):
        x += 1

        # Update decision parameter
        if d < 0:
            d += dy
        else:
            d += dy - dx
            y += 1

        # Plot the pixel
        draw_pixel(x, y)

    glEnd()
    glFlush()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, display[0], 0, display[1], -1, 1)

    glPointSize(5)
    glBegin(GL_POINTS)

    # Set starting and ending points
    x0, y0 = 0, 2
    x1, y1 = -5, 4

    # Draw the line using the Midpoint Line-Drawing Algorithm
    draw_line_midpoint(x0, y0, x1, y1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
