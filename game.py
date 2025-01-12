import pygame
from start_menu import StartMenu
from game_model import GameModel
from game_control import GameControl
from game_view import GameView
from setting import *

class Game:
    def __init__(self):
        self.start_menu = StartMenu() #開始畫面
        self.reset_game()  # 重置遊戲
    def reset_game(self):
        self.start_menu.page = 0 #起始頁面
        self.game_state = GAME_START
        pygame.mixer.music.stop()  # 重置遊戲時停止音樂
        if self.start_menu.selected_mode == 'easy': #簡單模式音樂
            pygame.mixer.music.load('audio/bgm1.mp3') 
            pygame.mixer.music.set_volume(0.4)
        elif self.start_menu.selected_mode == 'hard': #困難模式音樂
            pygame.mixer.music.load('audio/bgm2.mp3')
            pygame.mixer.music.set_volume(0.2)
        self.model = GameModel(self.start_menu.selected_mode) #MVC
        self.control = GameControl(self.model)
        self.view = GameView(self.model.background,self.model.player, self.model.interface, self.model.towers, self.model.enemy_towers, 
                            self.model.soldiers, self.model.enemies, self.start_menu, self.model.money_icon, self.model.time_icon)
    def handle_click(self, pos):
        if self.game_state == GAME_START:
            selected_mode = self.start_menu.handle_click(pos)  # 開始畫面的點擊事件
            if selected_mode: #開始畫面的按鈕被點擊
                self.start_menu.selected_mode = selected_mode
                self.reset_game()  # 重置遊戲成選擇的模式
                self.game_state = GAME_RUNNING
        elif self.game_state == GAME_RUNNING:
                self.model.interface.handle_click(pos)  # 遊戲內的點擊事件
        return self.game_state
    def toggle_pause(self):
        if self.game_state in [GAME_RUNNING, GAME_PAUSED]: #遊戲進行中切換狀態
            self.game_state = GAME_PAUSED if self.game_state == GAME_RUNNING else GAME_RUNNING
            self.control.toggle_timer() #切換計時
    def manage_music(self): #管理音樂
        if self.game_state in [GAME_RUNNING, GAME_PAUSED]: #遊戲進行中撥放音樂
            if not pygame.mixer.music.get_busy():  
                pygame.mixer.music.play(-1)       # 循環播放背景音樂
        else: #遊戲結束
            if pygame.mixer.music.get_busy():    
                pygame.mixer.music.stop()        # 停止播放音樂
    def update(self): #更新遊戲
        self.game_state = self.control.update(self.game_state)
        self.manage_music()
    def draw(self, screen):
        if self.game_state == GAME_START: #繪製開始畫面
            self.view.draw_start_screen(screen)
        elif self.game_state in [GAME_RUNNING, GAME_OVER, GAME_PAUSED]: #繪製遊戲畫面
            self.view.draw_game_interface(screen, self.control.global_time)
            if self.game_state in [GAME_OVER, GAME_PAUSED]: #繪製遊戲狀態訊息
                self.view.draw_game_state_message(screen, self.game_state, self.model.towers.hp, self.model.enemy_towers.hp)
