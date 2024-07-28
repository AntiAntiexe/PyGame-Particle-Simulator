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

                velocity1 = v1 - (2 * self.particle2.m) / (self.particle1.m + self.particle2.m) * (np.dot((v1 - v2), (self.particle1.pos[0] - self.particle2.pos[0]))) / ((math.sqrt(abs(self.particle1.pos[0] - self.particle2.pos[0]) ** 2)) ** 2) * (self.particle1.pos[0] - self.particle2.pos[0])
                velocity2 = v2 - (2 * self.particle1.m) / (self.particle1.m + self.particle2.m) * (np.dot((v2 - v1), (self.particle2.pos[0] - self.particle1.pos[0]))) / ((math.sqrt(abs(self.particle2.pos[0] - self.particle1.pos[0]) ** 2)) ** 2) * (self.particle2.pos[0] - self.particle1.pos[0])
            # Wall collisions particle one


            '''
            This code is to be put in particles.py as it does not reference any other particles.
            
            if pos_1[0] - r1 <= 0 or pos_1[0] + r1 >= space_size:
                velocity1 = -velocity1

            if pos_1[1] - r1 <= 0 or pos_1[1] + r1 >= space_size:
                gravity1 = -gravity1

            if pos_2[0] - r2 <= 0 or pos_2[0] + r2 >= space_size:
                velocity2 = -velocity2

            if pos_2[1] - r2 <= 0 or pos_2[1] + r2 >= space_size:
                gravity2 = -gravity2
                '''

            # Flip the display
            pygame.display.flip()

'''
this code is also to be put in particles.py as it does not reference any other particles.

            pos_1[1] = pos_1[1] + gravity1 * dt

            pos_1[0] = pos_1[0] + velocity1 * dt

            pos_2[1] = pos_2[1] + gravity2 * dt

            pos_2[0] = pos_2[0] + velocity2 * dt

            print(pos_1[0], pos_1[1], pos_2[0], pos_2[1])

'''
            # limit frame rate to desired number of frames per second.

            self.clock.tick(self.rate)

        # Done! Time to quit.
        pygame.quit()



