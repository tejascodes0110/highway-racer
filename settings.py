import pygame

# Screen Dimensions
WIDTH = 800
HEIGHT = 600

# Frame Rate
FPS = 60

# Road & Lane Coordinates
# 3 equal lanes across 800px width
LANE_WIDTH = WIDTH // 3  # ~266px
LANES = [
    LANE_WIDTH // 2,                     # Lane 0 (Left):   ~133px
    LANE_WIDTH + (LANE_WIDTH // 2),      # Lane 1 (Middle): ~400px
    (2 * LANE_WIDTH) + (LANE_WIDTH // 2) # Lane 2 (Right):  ~666px
]

# Color Palette (RGB Tuples)
COLOR_ASPHALT = (40, 40, 40)
COLOR_YELLOW = (255, 255, 0)
COLOR_PLAYER = (0, 255, 255)
COLOR_ENEMY = (255, 69, 0)
COLOR_UI = (255, 255, 255)
COLOR_POWERUP = (0, 255, 0)

# Initial Speeds & Timers
BASE_SPEED = 5
ENEMY_SPAWN_INTERVAL = 1500   # Milliseconds
POWERUP_SPAWN_INTERVAL = 5000 # Milliseconds
POWERUP_DURATION = 3000       # Milliseconds