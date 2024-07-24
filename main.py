import pygame


# Particle One
x1 = 125
velocity1 = -50
radius1 = 10


# Particle Two
x2 = 375
velocity2 = 50
radius2 = 10

# Simulation parameters
space_size = 500
colour = (255,255, 250)
rate = 60 # fps
dt = 1/rate # times step between frames

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
    pygame.draw.circle(screen, colour, (x1, 250),radius1)

    # Draw a solid white circle in the center
    pygame.draw.circle(screen, colour, (x2, 250), radius2)


    # Wall collisions particle one
    if x1-radius1 <= 0 or x1+radius1 >= space_size:
        velocity1 = -velocity1

    # Wall collisions particle two
    if x2-radius2 <= 0 or x2+radius2 >= space_size:
        velocity2 = -velocity2

    # Flip the display
    pygame.display.flip()


    # Partcile Dynamics for particle one
    x1 = x1 + velocity1*dt

    # Partcile Dynamics for particle two
    x2 = x2 + velocity2 * dt

    # limit frame rate to desired number of frames per second.

    clock.tick(rate)

# Done! Time to quit.
pygame.quit()