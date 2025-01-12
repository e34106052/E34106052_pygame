import pygame
import sys
from setting import *
from game import Game

#初始化遊戲設定
pygame.init()
pygame.font.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Clothes!!")
clock = pygame.time.Clock()

game = Game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        if event.type == pygame.KEYDOWN: # 處理按鈕事件
            if event.key == pygame.K_p:  # 按 P 鍵來切換暫停
                game.toggle_pause()
            if event.key == pygame.K_r and (game.game_state == GAME_OVER or game.game_state == GAME_PAUSED):  # 按 R 鍵來重開
                game.reset_game()
            if game.game_state == GAME_RUNNING:
                game.view.interface.handle_keypress(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_click(event.pos)  # 處理點擊事件
    game.update()  #更新遊戲狀態
    game.draw(screen) #繪製畫面
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
