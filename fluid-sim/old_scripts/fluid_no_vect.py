import pygame
import numpy as np
import math



space_size = 500

rate = 60 # fps
dt = 1/rate # times step between frames

# Particle One
y1 = 125
x1 = 125
#collisionDamp = 1
velocity1 = 150
gravity1 = 50
r1 = 10
m1 = 1
colour1 = (0, 0, 250)

# Particle two
y2 = 125
x2 = 20
collisionDamp = 1
velocity2 = 100
gravity2 = 50
r2 = 10
m2 = 1
colour2 = (255, 0, 250)

# Simulation parameters


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([space_size, space_size])

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Draw a solid white circle in the center
    pygame.draw.circle(screen, colour1, (x1, y1),r1)

    # Draw a solid white circle in the center
    pygame.draw.circle(screen, colour2, (x2, y2), r2)

    if abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) < r1+r2:
        v1, v2 = velocity1, velocity2

        velocity1 = v1 - (2 * m2)/(m1 + m2) * (np.dot((v1 - v2), (x1 - x2)))/((math.sqrt(abs(x1- x2)**2))**2) * (x1 - x2)
        velocity2 = v2 - (2 * m1) / (m1 + m2) * (np.dot((v2 - v1), (x2 - x1))) / ((math.sqrt(abs(x2 - x1) ** 2)) ** 2) * (x2 - x1)
    # Wall collisions particle one
    if x1-r1 <= 0 or x1+r1 >= space_size:
        velocity1 = -velocity1

    if y1-r1 <= 0 or y1+r1 >= space_size:
        gravity1 = -gravity1
        #y1 = (y1-r1) * y1
        #gravity *= -1 * collisionDamp

    if x2-r2 <= 0 or x2+r2 >= space_size:
        velocity2 = -velocity2

    if y2-r2 <= 0 or y2+r2 >= space_size:
        gravity2 = -gravity2
        #y1 = (y1-r1) * y1
        #gravity *= -1 * collisionDamp

    # Flip the display
    pygame.display.flip()

    y1 = y1 + gravity1 * dt

    x1 = x1 + velocity1 * dt

    y2 = y2 + gravity2 * dt

    x2 = x2 + velocity2 * dt



    # limit frame rate to desired number of frames per second.

    clock.tick(rate)

# Done! Time to quit.
pygame.quit()