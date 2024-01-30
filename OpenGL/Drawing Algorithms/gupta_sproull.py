import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_pixel(x, y, intensity):
    glColor(intensity, intensity, intensity)
    glVertex2f(x, y)


def draw_line_gupta_sproull(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    # Determine the steps along the x and y axes
    steps = max(abs(dx), abs(dy))

    # Calculate increments
    x_increment = dx / steps
    y_increment = dy / steps

    # Initial coordinates
    x, y = x0, y0

    # Plot the first pixel
    draw_pixel(x, y, 1)

    # Main loop
    for i in range(int(steps)):
        x += x_increment
        y += y_increment

        # Plot the pixel
        draw_pixel(x, y, 1)

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
    x0, y0 = 4, 3
    x1, y1 = 12, -5

    # Draw the line using Gupta-Sproull algorithm
    draw_line_gupta_sproull(x0, y0, x1, y1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
