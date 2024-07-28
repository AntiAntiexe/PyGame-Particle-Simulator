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



