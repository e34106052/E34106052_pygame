import pygame
from setting import *
from background import Background, Button
from button_manager import SummonManager, UpgradeManager
from unit import Soldier_normal, Soldier_speed, Soldier_people

class Interface:
    def __init__(self, image_path, x, y, width, height, soldiers, player_tower, money=1000):
        self.image = Background(x, y, width, height, image_path)
        self.money = money
        self.player_tower = player_tower
        #互動按鈕
        self.switch_button = Button(x + 900, y + 70, 100, 100, 'image/switch.png')  
        self.summon_button1 = Button(x + 100, y + 70, 100, 100, 'image/summon1.png')
        self.summon_button2 = Button(x + 300, y + 70, 100, 100, 'image/summon2.png')
        self.summon_button3 = Button(x + 500, y + 70, 100, 100, 'image/summon3.png')
        self.upgrade_button1 = Button(x + 100, y + 70, 100, 100, 'image/upgrade1.png')
        self.upgrade_button2 = Button(x + 300, y + 70, 100, 100, 'image/upgrade2.png')
        #未解鎖按鈕
        self.summon_button2_lock = Button(x + 300, y + 70, 100, 100, 'image/lock2.png')
        self.summon_button3_lock = Button(x + 500, y + 70, 100, 100, 'image/lock2.png')
        self.upgrade_button2_lock = Button(x + 300, y + 70, 100, 100, 'image/lock.png')
        self.summon_button2_unlock = 5 
        self.summon_button3_unlock = 15
        self.upgrade_button2_unlock = 3   
        #互動按鈕操作
        self.summon_manager1 = SummonManager(soldiers, player_tower, soldier= Soldier_normal, summon_cost= 60) 
        self.summon_manager2 = SummonManager(soldiers, player_tower, soldier= Soldier_speed, summon_cost= 100)
        self.summon_manager3 = SummonManager(soldiers, player_tower, soldier= Soldier_people, summon_cost= 700)
        self.upgrade_manager = UpgradeManager(player_tower)
        self.current_menu = 0  # 初始為召喚頁面
    def handle_click(self, pos):
        if self.switch_button.is_clicked(pos):  # 切換界面
            self.current_menu = 1 - self.current_menu
            return
        # 定義按鈕對應的動作
        actions = {
            0: [  # 召喚界面
                (self.summon_button1, self.summon_manager1, None),  # 無解鎖條件
                (self.summon_button2, self.summon_manager2, self.summon_button2_unlock),
                (self.summon_button3, self.summon_manager3, self.summon_button3_unlock),
            ],
            1: [  # 升級界面
                (self.upgrade_button1, self.upgrade_manager.upgrade_health, None),
                (self.upgrade_button2, self.upgrade_manager.upgrade_cannon, self.upgrade_button2_unlock),
            ],
        }
        # 檢查當前頁面的按鈕點擊
        for button, action, unlock_level in actions.get(self.current_menu, []):
            if button.is_clicked(pos) and (unlock_level is None or self.player_tower.level >= unlock_level):
                cost = action.summon_soldier(self.money) if hasattr(action, 'summon_soldier') else action(self.money)
                self.money -= cost  # 扣除金錢
    def handle_keypress(self, key):
        if key == pygame.K_SPACE:  # 切換界面
            self.current_menu = 1 - self.current_menu
            return
        # 定義按鍵對應的動作
        key_actions = {
            0: {  # 召喚界面
                pygame.K_s: (self.summon_manager1.summon_soldier, None), 
                pygame.K_d: (self.summon_manager2.summon_soldier, self.summon_button2_unlock),     
                pygame.K_f: (self.summon_manager3.summon_soldier, self.summon_button3_unlock),    
            },
            1: {  # 升級界面
                pygame.K_s: (self.upgrade_manager.upgrade_health, None),  
                pygame.K_d: (self.upgrade_manager.upgrade_cannon, self.upgrade_button2_unlock),     
            }
        }
        # 根據當前界面和按鍵執行對應行為
        for action_key, (action, unlock_level) in key_actions.get(self.current_menu, {}).items():
            if key == action_key and (unlock_level is None or self.player_tower.level >= unlock_level):
                cost = action(self.money)
                self.money -= cost
    def draw(self, screen):
        self.image.draw(screen)
        self.switch_button.draw(screen)
        # 繪製按鈕和相關文字
        def draw_button(button, lock_button, level_req, cost, pos): 
            if self.player_tower.level >= level_req: #檢查是否解鎖
                button.draw(screen)
                cost_text = FONT(18).render(f"${cost:^4}", True, YELLOW)
            else: #未解鎖
                lock_button.draw(screen)
                cost_text = FONT(18).render(f" Lv{level_req}", True, YELLOW)
            screen.blit(cost_text, pos)
        # 繪製召喚界面
        if self.current_menu == 0:
            draw_button(self.summon_button1, None, 0, self.summon_manager1.summon_cost, (120, 662))
            draw_button(self.summon_button2, self.summon_button2_lock, self.summon_button2_unlock, self.summon_manager2.summon_cost, (320, 662))
            draw_button(self.summon_button3, self.summon_button3_lock, self.summon_button3_unlock, self.summon_manager3.summon_cost, (520, 662))
        # 繪製升級界面
        elif self.current_menu == 1:
            draw_button(self.upgrade_button1, None, 0, self.upgrade_manager.upgrade_health_cost, (120, 662))
            draw_button(self.upgrade_button2, self.upgrade_button2_lock, self.upgrade_button2_unlock, self.upgrade_manager.upgrade_cannon_cost, (320, 662))
        # 繪製金錢資訊
        money_text = FONT(28).render(f"{self.money}", True, BLACK)
        screen.blit(money_text, (110, 18))

