import pygame
import random
import settings

class PowerUp:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.type = "freeze"
        self.active = True
        
        # Pick a random lane (0, 1, or 2)
        self.lane = random.randint(0, 2)
        
        # Position the powerup based on the selected lane
        self.x = settings.LANES[self.lane] - self.width // 2
        # Start above the screen
        self.y = random.randint(-200, -50)
        self.speed = settings.BASE_SPEED

    def update(self):
        # Move downward at a steady speed
        self.y += self.speed

    def draw(self, surface):
        # Render as a distinct glowing shape (rounded rectangle/circle)
        pygame.draw.rect(surface, settings.COLOR_POWERUP, 
                         (self.x, self.y, self.width, self.height), 
                         border_radius=15)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        return self.y > settings.HEIGHT
