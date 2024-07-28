import numpy as np
import pygame
import math

class Model:
    def __init__(self, fluid, pos, velocity, gravity, radius, mass, colour):
        self.fluid = fluid
        self.pos = pos
        self.v = velocity
        self.gravity = gravity
        self.r = radius
        self.m = mass
        self.colour = colour

    def create(self):
        pygame.draw.circle(self.fluid.screen, self.colour, self.pos, self.r)

    def x_wallCollision(self):
        if self.pos[0] - self.r <= 0 or self.pos[0] + self.r >= self.fluid.space_size:
            self.v = self.v * -1
            print('HIT X')


    def y_wallCollision(self):
        if self.pos[1] - self.r <= 0 or self.pos[1] + self.r >= self.fluid.space_size:
            self.v = self.v * -1
            print('HIT Y')

    def xmovement(self):
        self.pos[0] = self.pos[0] + self.v * self.fluid.dt
    def ymovement(self):
        self.pos[1] = self.pos[1] + self.gravity * self.fluid.dt







