import pygame


# Particle One
x1 = 125
velocity1 = 0
r1 = 10
m1 = 1
colour1 = (0, 0, 250)


# Particle Two
x2 = 375
velocity2 = -50
r2 = 31.6
m2 = 1000000
colour2 = (255,255, 255)
count = 0

c = 1

# Simulation parameters
space_size = 500

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
    pygame.draw.circle(screen, colour1, (x1, 250),r1)

    # Draw a solid white circle in the center
    pygame.draw.circle(screen, colour2, (x2, 250), r2)


    # Particle to particle collisions
    if abs(x2 - x1) < r1+r2:
        ux1, ux2 = velocity1, velocity2
        #velocity1 = ux1 * (m1 - m2)/(m1 + m2) + 2 * ux2 * m2/(m1+m2)
        #velocity2 = 2 * ux1 * m1/(m1+m2) + ux2 * (m2 - m1)/(m1+m2)

        velocity1 = ((c*m2)*(ux2 - ux1) + m1*ux1 + m2*ux2)/m1+m2
        velocity2 = ((c * m2) * (ux1 - ux2) + m1 * ux1 + m2 * ux2) / m1 + m2
        count = count+1
        print(count)

    # Wall collisions particle one
    if x1-r1 <= 0 or x1+r1 >= space_size:
        velocity1 = -velocity1
        count = count + 1
        print(count)

    # Wall collisions particle two
    if x2-r2 <= 0: #or x2+r2 >= space_size:
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