import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius) 
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        pos_vec = self.position.rotate(split_angle)
        neg_vec = self.position.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(pos_vec.x, pos_vec.y, new_radius)
        asteroid.velocity += self.velocity * 1.2
        asteroid = Asteroid(neg_vec.x, neg_vec.y, new_radius)
        asteroid.velocity += self.velocity * 1.2