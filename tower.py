import pygame
import math
from bullet import Bullet
from background import Background
from setting import *

class BaseTower(pygame.sprite.Sprite):
    def __init__(self, image, x, y, hp, color=GREEN, w=150, h=150):
        super().__init__()
        self.image = Background(x, y, w, h, image)
        #塔的數值
        self.hp = hp
        self.max_hp = hp
        self.level = 1
        self.color = color #血條顏色
    def upgrade(self): #升級塔
        pass
    def draw(self, screen):        
        self.image.draw(screen)
        #繪製塔的血條
        health_bar_width = self.image.rect.width * 0.8
        health_bar_height = 10
        health_percentage = self.hp / self.max_hp
        pygame.draw.rect(screen, RED, (self.image.rect.x + 10, self.image.rect.y - 25, health_bar_width, health_bar_height))
        #塔目前剩餘血量數值
        pygame.draw.rect(screen, self.color, (self.image.rect.x + 10, self.image.rect.y - 25, health_bar_width * health_percentage, health_bar_height))
        #繪製資訊
        hp_text = FONT(16).render(f"{self.hp}/{self.max_hp}", True, self.color) 
        lv_text = FONT(16).render(f"Lv:{self.level}", True, WHITE)
        screen.blit(hp_text, (self.image.rect.x + health_bar_width/2 -20  , self.image.rect.y -45))
        screen.blit(lv_text, (self.image.rect.x + health_bar_width/2 -10  , self.image.rect.y-10))

class PlayerTower(BaseTower):
    def __init__(self, image, x, y, hp, cannon_image):
        super().__init__(image, x, y, hp)
        #玩家塔砲台設定
        self.angle = 0
        self.max_angle = 45 #可調整角度
        self.cannon_image = pygame.image.load(cannon_image)
        self.cannon_image = pygame.transform.scale(self.cannon_image, (80, 40))  
        self.cannon_level = 1
        self.attack_power = 25 #砲台傷害
        #子彈設定
        self.bullets = pygame.sprite.Group()
        self.bullet_ready = True
        self.bullet_time = 0
        self.bullet_delay = 900 #冷卻時間
    def get_user_input(self):
        keys = pygame.key.get_pressed()
        #按a發射子彈並進入冷卻
        if keys[pygame.K_a] and self.bullet_ready:
            self.bullet_ready = False
            bullet = Bullet(self.image.rect.right, self.image.rect.top + 50, self.angle)
            self.bullets.add(bullet)
            self.bullet_time = pygame.time.get_ticks()
        #按上下調整砲台角度
        if keys[pygame.K_UP]:
            self.angle -= math.radians(1)
        if keys[pygame.K_DOWN]:
            self.angle += math.radians(1)
    def constrain_movement(self): # 限制砲台角度
        if self.angle <= math.radians(-self.max_angle):
            self.angle = math.radians(-self.max_angle)
        if self.angle >= math.radians(self.max_angle):
            self.angle = math.radians(self.max_angle)
    def recharge_bullet(self): #子彈冷卻
        if not self.bullet_ready:
            now = pygame.time.get_ticks()
            if now - self.bullet_time >= self.bullet_delay:
                self.bullet_ready = True
    def upgrade_health(self): #升級設定
        self.level += 1
        self.hp += 20  
        self.max_hp += 20 # 提高生命值上限
    def upgrade_cannon(self):
        self.cannon_level += 1
        self.attack_power *=1.2  # 提高攻擊力  
    def draw(self, screen):
        super().draw(screen)  # 繪製塔和血條
        rotated_cannon = pygame.transform.rotate(self.cannon_image, math.degrees(-self.angle))
        cannon_rect = rotated_cannon.get_rect(center=(self.image.rect.right, self.image.rect.top + 50))
        lv_text = FONT(16).render(f"Lv:{self.cannon_level}", True, WHITE)
        screen.blit(lv_text, (self.image.rect.x + 135 , self.image.rect.y))
        screen.blit(rotated_cannon, cannon_rect) # 繪製炮台
        self.bullets.draw(screen)  # 繪製子彈
    def update(self):
        self.recharge_bullet()
        self.get_user_input()
        self.constrain_movement()
        self.bullets.update()

class EnemyTower(BaseTower):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y + 50, hp, color=YELLOW, h=100) #設定敵人數值
    def upgrade(self):
        self.level += 1
        self.hp += 100 
        self.max_hp +=100 # 提高生命值上限  
    def update(self):
        pass
