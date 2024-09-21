import pygame
import numpy as np
import math
from particles import Model


class Fluid():
    def __init__(self):
        self.space_size = 500

        self.rate = 60 # fps
        self.dt = 1/self.rate # times step between frames

        # Particle One
        self.particle1 = Model(self, pos=np.array([125, 125], dtype=np.float64), velocity=50, gravity=50
                              , radius=10, mass=1, colour=(0, 0, 250))

        # Particle Two
        self.particle2 = Model(self, pos=np.array([20, 125], dtype=np.float64), velocity=50, gravity=50
                              , radius=10, mass=1, colour=(255, 0, 250))

        pygame.init()

        # Set up the drawing window
        self.screen = pygame.display.set_mode([self.space_size, self.space_size])

        self.clock = pygame.time.Clock()

    def run(self):

        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with black
            self.screen.fill((0, 0, 0))

            # Draw a solid white circle in the center
            self.particle1.create()

            # Draw a solid white circle in the center
            self.particle2.create()

            if abs(math.sqrt((self.particle2.pos[0] - self.particle1.pos[0]) ** 2 + (self.particle2.pos[1] - self.particle1.pos[1]) ** 2)) < self.particle1.r + self.particle2.r:
                v1, v2 = self.particle1.v, self.particle2.v

                self.particle1.v = v1 - (2 * self.particle2.m) / (self.particle1.m + self.particle2.m) * (np.dot((v1 - v2), (self.particle1.pos[0] - self.particle2.pos[0]))) / ((math.sqrt(abs(self.particle1.pos[0] - self.particle2.pos[0]) ** 2)) ** 2) * (self.particle1.pos[0] - self.particle2.pos[0])
                self.particle2.v = v2 - (2 * self.particle1.m) / (self.particle1.m + self.particle2.m) * (np.dot((v2 - v1), (self.particle2.pos[0] - self.particle1.pos[0]))) / ((math.sqrt(abs(self.particle2.pos[0] - self.particle1.pos[0]) ** 2)) ** 2) * (self.particle2.pos[0] - self.particle1.pos[0])
            # Wall collisions particle one


            self.particle1.x_wallCollision()
            self.particle1.y_wallCollision()

            self.particle2.x_wallCollision()
            self.particle2.y_wallCollision()

            # Flip the display
            pygame.display.flip()


            # Define moevement
            self.particle1.xmovement()
            self.particle2.xmovement()
            self.particle1.ymovement()
            self.particle2.ymovement()

            #print(self.particle1.pos[0], self.particle1.pos[1], self.particle2.pos[0], self.particle2.pos[1])


            # limit frame rate to desired number of frames per second.

            self.clock.tick(self.rate)

        # Done! Time to quit.
        pygame.quit()


Fluid().run()


