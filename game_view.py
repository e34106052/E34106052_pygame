from setting import *

class GameView:
    def __init__(self, background,player, interface, towers, enemy_towers, soldiers, enemies, start_menu,money_icon, time_icon):
        self.background = background #基本物件建立
        self.player = player
        self.interface = interface
        self.towers = towers
        self.enemy_towers = enemy_towers
        self.soldiers = soldiers
        self.enemies = enemies
        self.start_menu = start_menu
        self.money_icon = money_icon
        self.time_icon = time_icon
    def draw_start_screen(self, screen): #繪製開始畫面
        self.start_menu.draw(screen)
    def draw_game_interface(self, screen, global_time): #繪製遊戲界面
        self.background.draw(screen)
        self.money_icon.draw(screen)
        self.time_icon.draw(screen)
        self.interface.draw(screen)
        self.towers.draw(screen)
        self.player.draw(screen)
        self.enemy_towers.draw(screen)
        for soldier in self.soldiers:# 繪製所有士兵和敵人
            soldier.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen) 
        minutes = global_time // 60000 # 繪製計時資訊
        seconds = (global_time // 1000) % 60
        timer_text = FONT(34).render(f"{minutes:02}:{seconds:02}", True, BLACK)
        screen.blit(timer_text, (SCREEN_WIDTH - 135, 18))
    def draw_game_state_message(self, screen, game_state, towers_hp, enemy_towers_hp): #繪製遊戲狀態訊息
        if game_state in [GAME_OVER, GAME_PAUSED]:
            message = ''
            message2 = ''
            message3 = ''
            setting = pygame.image.load('image/setting.png')
            setting = pygame.transform.scale(setting, (625, 250))
            screen.blit(setting, ((SCREEN_WIDTH-setting.get_width())//2, 60))
            if enemy_towers_hp <= 0:  # 勝利情況
                message = "Victory"
                message2 = 'Press R to restart'
            elif towers_hp <= 0:  # 失敗情況
                message = "Defeat"
                message2 = 'Press R to restart'
            elif game_state == GAME_PAUSED: # 暫停情況
                message = "Paused"
                message2 = 'Press P to resume'
                message3 = 'Press R to restart'
            text = FONT(80).render(message, False, BLACK) # 繪製訊息
            text2 = FONT(36).render(message2, False, BLACK)
            text3 = FONT(36).render(message3, False, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100))
            screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, 180))
            screen.blit(text3, (SCREEN_WIDTH // 2 - text2.get_width() // 2, 220))
