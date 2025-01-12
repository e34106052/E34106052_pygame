import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        #設定子彈座標大小
        self.image = pygame.image.load('image/bullet.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #設定子彈角度及飛行速度
        self.angle = angle
        self.speed = 10
        self.vx = self.speed * math.cos(self.angle)  # 水平速度
        self.vy = self.speed * math.sin(self.angle)  # 垂直速度
        self.gravity = 0.2  # 重力加速度        
    def update(self):
        self.rect.x += self.vx  # 更新子彈位置
        self.rect.y += self.vy
        self.vy += self.gravity # 增加重力影響
        if self.rect.y >= 520:   
            self.kill()  # 掉出畫面則刪除物件
