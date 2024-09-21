import pygame
import numpy as np
import math


space_size = 500

rate = 60  # fps
dt = 1 / rate  # times step between frames

# Particle One
pos_1 = np.array([125, 125], dtype=np.float64)
# collisionDamp = 1
velocity1 = 300
gravity1 = 50
r1 = 10
m1 = 1
colour1 = (0, 0, 250)

# Particle two
pos_2 = np.array([20, 125], dtype=np.float64)
collisionDamp = 1
velocity2 = 300
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
    pygame.draw.circle(screen, colour1, pos_1, r1)

    # Draw a solid white circle in the center
    pygame.draw.circle(screen, colour2, pos_2, r2)

    if (
        abs(math.sqrt((pos_2[0] - pos_1[0]) ** 2 + (pos_2[1] - pos_1[1]) ** 2))
        < r1 + r2
    ):
        v1, v2 = velocity1, velocity2

        velocity1 = v1 - (2 * m2) / (m1 + m2) * (
            np.dot((v1 - v2), (pos_1[0] - pos_2[0]))
        ) / ((math.sqrt(abs(pos_1[0] - pos_2[0]) ** 2)) ** 2) * (pos_1[0] - pos_2[0])
        velocity2 = v2 - (2 * m1) / (m1 + m2) * (
            np.dot((v2 - v1), (pos_2[0] - pos_1[0]))
        ) / ((math.sqrt(abs(pos_2[0] - pos_1[0]) ** 2)) ** 2) * (pos_2[0] - pos_1[0])
    # Wall collisions particle one
    if pos_1[0] - r1 <= 0 or pos_1[0] + r1 >= space_size:
        velocity1 = -velocity1

    if pos_1[1] - r1 <= 0 or pos_1[1] + r1 >= space_size:
        gravity1 = -gravity1
        # y1 = (y1-r1) * y1
        # gravity *= -1 * collisionDamp

    if pos_2[0] - r2 <= 0 or pos_2[0] + r2 >= space_size:
        velocity2 = -velocity2

    if pos_2[1] - r2 <= 0 or pos_2[1] + r2 >= space_size:
        gravity2 = -gravity2
        # y1 = (y1-r1) * y1
        # gravity *= -1 * collisionDamp

    # Flip the display
    pygame.display.flip()

    pos_1[1] = pos_1[1] + gravity1 * dt

    pos_1[0] = pos_1[0] + velocity1 * dt

    pos_2[1] = pos_2[1] + gravity2 * dt

    pos_2[0] = pos_2[0] + velocity2 * dt

    print(pos_1[0], pos_1[1], pos_2[0], pos_2[1])

    # limit frame rate to desired number of frames per second.

    clock.tick(rate)

# Done! Time to quit.
pygame.quit()

