import pygame
import random
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.speed = 100
        self.direction = 0
        self.kind = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        random_angle_pos = self.velocity.rotate(random_angle)
        random_angle_neg = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        Asteroid(self.position.x, self.position.y, new_radius).velocity = random_angle_pos * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = random_angle_neg * 1.2
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return