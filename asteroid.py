import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), tuple(self.position), self.radius, 2)
    
    def update(self, dt):
       self.position += self.velocity * dt