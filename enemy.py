import pygame
import random
import settings

class Enemy:
    def __init__(self, lane=None):
        self.width = 50
        self.height = 80
        
    
        if lane is None:
            self.lane = random.randint(0, 2)
        else:
            self.lane = lane
            
       
        self.x = settings.LANES[self.lane] - self.width // 2
 
        self.y = random.randint(-200, -50)
        self.speed = settings.BASE_SPEED
        
    def update(self, current_game_speed=None):

        speed = current_game_speed if current_game_speed else self.speed
        self.y += speed

    def draw(self, surface):
 
        pygame.draw.rect(surface, settings.COLOR_ENEMY, 
                         (self.x, self.y, self.width, self.height), 
                         border_radius=10)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
  
        return self.y > settings.HEIGHT
