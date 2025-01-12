import pygame
from setting import *


class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, hp=10, dmg=10, speed=1, width=30,height=30, color=GREEN):
        super().__init__()
        # 設定單位圖片與大小
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # 設定單位數值
        self.hp = hp
        self.max_hp = hp
        self.dmg = dmg
        self.speed = speed
        self.color = color

    def take_damage(self, damage): #單位受到傷害
        self.hp -= damage
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        health_bar_width = self.rect.width #繪製血條
        health_bar_height = 5
        health_percentage = max(self.hp / self.max_hp, 0)  # 確保血量顯示不會低於0
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y - 10, health_bar_width * health_percentage, health_bar_height))

class Soldier(Unit): #士兵基類
    def __init__(self, x, y, image_path, hp, dmg, speed=1, width=30, height=30):
        super().__init__(x, y, image_path, hp, dmg, speed=speed)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.value = 0
    def update(self): #士兵向右移動
        self.rect.x += self.speed
class Soldier_normal(Soldier): #普通士兵
    def __init__(self, x, y, image_path="image/soldier_normal.png"):
        super().__init__(x, y, image_path, hp=70, dmg=10, speed=1)
class Soldier_speed(Soldier): #速度士兵
    def __init__(self, x, y, image_path="image/soldier_speed.png"):
        super().__init__(x, y, image_path, hp=50, dmg=25, speed=3)
class Soldier_people(Soldier): #強化士兵
    def __init__(self, x, y, image_path="image/soldier_people.png"):
        super().__init__(x, y, image_path, hp=180, dmg=50, speed=2)

class Enemy(Unit): #敵人基類
    def __init__(self, x, y, value, image_path, hp, dmg, speed=1, color=YELLOW):
        super().__init__(x, y, image_path, hp, dmg, speed=speed, color=color)
        self.value = value  # 死亡後的獎勵金錢
    def update(self): #敵人向左移動
        self.rect.x -= self.speed

class Enemy_normal(Enemy): #普通敵人
    def __init__(self, x, y, image_path="image/enemy_normal.png"):
        super().__init__(x, y, value=120, image_path=image_path, hp=100, dmg=15, speed=1)
class Enemy_elite(Enemy): #精英敵人
    def __init__(self, x, y, image_path="image/enemy_elite.png"):
        super().__init__(x, y, value=180, image_path=image_path, hp=200, dmg=20, speed=1)
class Enemy_speed(Enemy): #速度敵人
    def __init__(self, x, y, image_path="image/enemy_speed.png"):
        super().__init__(x, y, value=70, image_path=image_path, hp=60, dmg=20, speed=3)
class Enemy_tank(Enemy): #坦克敵人
    def __init__(self, x, y, image_path="image/enemy_tank.png"):
        super().__init__(x, y, value=250, image_path=image_path, hp=300, dmg=10, speed=1)
