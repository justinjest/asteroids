from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        self.radius = SHOT_RADIUS
        super().__init__(x,y, self.radius)
        self.velocity = 0
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def move (self, dt):
        self.velocity += self.velocity * dt
