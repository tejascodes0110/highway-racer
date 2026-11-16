import pygame
import sys
import settings
from player import Player
from enemy import Enemy
from score_manager import ScoreManager

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Highway Racer")
        self.clock = pygame.time.Clock()
        
        
        try:
            self.font = pygame.font.SysFont("Arial", 32)
            self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        except Exception:
            self.font = pygame.font.Font(None, 36)
            self.title_font = pygame.font.Font(None, 52)
        
        self.state = "START_SCREEN"
        self.running = True

    
        self.SPAWN_ENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_ENEMY, settings.ENEMY_SPAWN_INTERVAL)

        self.reset_game()

        self.score_manager = ScoreManager()
        self.highscore = self.score_manager.load_highscore()
        


    def reset_game(self):
        self.player = Player()
        self.enemies = []
        self.score = 0
        self.speed = settings.BASE_SPEED

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == "START_SCREEN":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset_game()
                    self.state = "PLAYING"
            
            elif self.state == "PLAYING":
                
                self.player.handle_event(event)

               
                if event.type == self.SPAWN_ENEMY:
                    self.enemies.append(Enemy())

            elif self.state == "GAME_OVER":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state = "PLAYING"
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False

    def update(self):
        if self.state == "PLAYING":
            self.player.update()
            
            player_rect = self.player.get_rect()

            for enemy in self.enemies[:]:
                enemy.update(self.speed)
                
                if player_rect.colliderect(enemy.get_rect()):
                    self.highscore = self.score_manager.save_highscore(self.score)
                    self.state = "GAME_OVER"

                if enemy.is_off_screen():
                    self.enemies.remove(enemy)
                    self.score += 10
                    
                    self.speed = settings.BASE_SPEED + (self.score // 30) * 1

    def draw(self):
        
        self.screen.fill(settings.COLOR_ASPHALT)
        
        
        line_x1 = settings.LANE_WIDTH
        line_x2 = settings.LANE_WIDTH * 2
        pygame.draw.line(self.screen, settings.COLOR_YELLOW, (line_x1, 0), (line_x1, settings.HEIGHT), 5)
        pygame.draw.line(self.screen, settings.COLOR_YELLOW, (line_x2, 0), (line_x2, settings.HEIGHT), 5)

        if self.state == "START_SCREEN":
            self.draw_text("HIGHWAY RACER", settings.WIDTH // 2, settings.HEIGHT // 3, True, font=self.title_font)
            self.draw_text("Press SPACE to Start", settings.WIDTH // 2, settings.HEIGHT // 2, True)
            self.draw_text("Controls: A / D or Left / Right Arrows", settings.WIDTH // 2, settings.HEIGHT // 2 + 50, True)

        elif self.state == "PLAYING":
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
            

            self.draw_text(f"Score: {self.score}", 20, 20, False)

        elif self.state == "GAME_OVER":
            self.draw_text("GAME OVER", settings.WIDTH // 2, settings.HEIGHT // 3 - 20, True, font=self.title_font)
            self.draw_text(f"Final Score: {self.score}", settings.WIDTH // 2, settings.HEIGHT // 2 - 20, True)
            self.draw_text(f"High Score: {self.highscore}", settings.WIDTH // 2, settings.HEIGHT // 2 + 20, True)
            self.draw_text("Press SPACE to Restart", settings.WIDTH // 2, settings.HEIGHT // 2 + 70, True)
            self.draw_text("Press ESC to Quit", settings.WIDTH // 2, settings.HEIGHT // 2 + 110, True)

        pygame.display.flip()

    def draw_text(self, text, x, y, center=False, font=None):
        render_font = font if font else self.font
        surface = render_font.render(text, True, settings.COLOR_UI)
        rect = surface.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        self.screen.blit(surface, rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(settings.FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameController()
    game.run()