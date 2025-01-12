import pygame

FPS = 40

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (230, 230, 250)

GAME_RUNNING = 1
GAME_PAUSED = 2
GAME_OVER = 3
GAME_START = 4
GAME_INFO = 5

def FONT(size):
    return pygame.font.Font('font/BoutiqueBitmap9x9.ttf', size) #預設像素字體