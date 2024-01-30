import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_pixel(x, y, intensity):
    glColor(intensity, intensity, intensity)
    glVertex2f(x, y)


def draw_line_xiaolin_wu(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    gradient = dy / dx if dx != 0 else 1  # Avoid division by zero

    # Initial coordinates
    x, y = x0, y0

    # Plot the first pixel
    draw_pixel(x, y, 1)

    # Calculate initial intensity
    intensity = 1.0

    # Main loop
    for i in range(int(dx)):
        x += 1
        y += gradient

        # Calculate fractional parts
        fy = y % 1

        # Calculate intensities for the two pixels
        intensity2 = fy
        intensity1 = 1 - fy

        # Plot the two pixels with intensity
        draw_pixel(x, int(y), intensity1)
        draw_pixel(x, int(y) + 1, intensity2)

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
    x0, y0 = 9, 6
    x1, y1 = 14, 3

    # Draw the line using Xiaolin Wu's algorithm
    draw_line_xiaolin_wu(x0, y0, x1, y1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
