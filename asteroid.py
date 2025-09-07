from circleshape import *
import pygame

Class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,raidus)
        
    def draw(self,screen):
        pygame.draw.cirlce(screen,"white", self.position, self.radius, 2)

    def update(self,dt):

