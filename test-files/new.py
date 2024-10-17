import pygame
y = 500
x = 200
r = 10
vel = 5

isJump = False
jumpCount = 10

rate = 60 # fps
dt = 1/rate # times step between frames

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 255, 0), (x, y), r, 0)



    if pygame.key.get_pressed()[pygame.K_s]:
        y = y + 10
    elif pygame.key.get_pressed()[pygame.K_a]:
        x = x - 10
    elif pygame.key.get_pressed()[pygame.K_d]:
        x = x + 10
    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        isJump = True

    if not (isJump):  # Checks is user is not jumping
        '''if pygame.key.get_pressed()[pygame.K_w] and y > vel:  # Same principles apply for the y coordinate
            y -= vel'''

        if pygame.key.get_pressed()[pygame.K_s] and y  < 500 - r - vel:
            y += vel

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:  # This will execute if our jump is finished
            jumpCount = 10
            isJump = False
        # This is what will happen if we are jumping

    if x-r <=0:
        x = x+10
    elif x+r >= 800:
        x = x-10
    elif y-r <=0:
        y = y+10
    elif y+r >= 600:
        y = y-10





    # Flip the display
    pygame.display.flip()

    # limit frame rate to desired number of frames per second.

    clock.tick(rate)

# Done! Time to quit.
pygame.quit()
