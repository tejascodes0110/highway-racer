import pygame
import settings

class Player:
    def __init__(self):
        self.width = 50
        self.height = 80
        self.current_lane = 1 
        self.speed = 10        
        
        self.x = settings.LANES[self.current_lane] - self.width // 2
        self.y = settings.HEIGHT - self.height - 20

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                if self.current_lane > 0:
                    self.current_lane -= 1
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                if self.current_lane < 2:
                    self.current_lane += 1
        
       
        self.x = settings.LANES[self.current_lane] - self.width // 2

    def update(self):
       
        pass

    def draw(self, surface):
        
        pygame.draw.rect(surface, settings.COLOR_PLAYER, 
                         (self.x, self.y, self.width, self.height), 
                         border_radius=10)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
