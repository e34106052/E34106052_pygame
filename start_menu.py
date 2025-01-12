import pygame
from setting import *
from background import Background, Button

class StartMenu:
    def __init__(self):
        self.image = Background(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 'image/start_menu.png') #開始畫面背景
        self.info = Background(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 'image/info.png') #遊戲說明背景
        # 主選單按鈕
        self.start_button = Button(400, 300, 300, 100, 'image/game_start.png') #開始按鈕
        self.info_button = Button(400, 450, 300, 100, 'image/how_to_play.png') #遊戲說明按鈕
        self.easy_button = Button(200, 500, 200, 100, 'image/easy.png') #簡單模式按鈕
        self.hard_button = Button(SCREEN_WIDTH-400, 500, 200, 100, 'image/hard.png') #困難模式按鈕
        self.up_button = Button(50, 50, 50, 50, 'image/up.png') #上一頁按鈕
        self.selected_mode = ''  #遊戲模式
        self.page = 0 #開始頁面
        self.click = pygame.mixer.Sound("audio/click.mp3") #按鈕音效 
    def handle_click(self, pos):
        if self.page != 0 and self.up_button.is_clicked(pos): #點擊上一頁按鈕
            self.page = 0
            self.click.play()
        if self.page == 0: #開始畫面選擇
            if self.start_button.is_clicked(pos):
                self.page = 1
                self.click.play()
            elif self.info_button.is_clicked(pos):
                self.page = 2
                self.click.play()
        elif self.page == 1: #遊戲模式選擇
            if self.easy_button.is_clicked(pos):
                self.selected_mode = 'easy'
                self.click.play()
                return 'easy'
            elif  self.hard_button.is_clicked(pos):
                self.selected_mode = 'hard'
                self.click.play()
                return 'hard'
        return None       
    def draw(self, screen):
        self.image.draw(screen) #繪製背景
        title_text = FONT(80).render("Two Clothes!!", True, BLACK) #繪製文字
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        #繪製不同頁面
        if self.page == 0:
            self.start_button.draw(screen)
            self.info_button.draw(screen)
        elif self.page == 1:
            self.easy_button.draw(screen)
            self.hard_button.draw(screen)
        elif self.page == 2:
            self.info.draw(screen)
        if self.page != 0:
            self.up_button.draw(screen)



