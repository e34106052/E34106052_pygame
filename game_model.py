import pygame
from background import Background
from tower import PlayerTower, EnemyTower
from interface import Interface
from unit import Enemy_normal, Enemy_elite, Enemy_speed, Enemy_tank
import random
from setting import *

class GameModel:
    def __init__(self, mode):
        self.start = Background(0, 0 , SCREEN_WIDTH, SCREEN_HEIGHT, 'image/start_menu.png') #背景
        self.towers = PlayerTower('image/tower.png', 30, 370, 100, "image/cannon.png") #玩家塔
        self.player = Background(80, 460, 45, 60, 'image/player.png') #玩家
        self.soldiers = pygame.sprite.Group() #士兵
        self.enemies = pygame.sprite.Group() #敵人
        self.money_icon = Background( 20, 10, 250, 50, 'image/money.png') #金錢圖示
        self.time_icon = Background( 870, 10, 200, 50, 'image/time.png') #時間圖示
        self.multiplier = 1
        if mode == 'easy': #簡單模式
            self.background = Background( 0, 0, SCREEN_WIDTH ,SCREEN_HEIGHT-200, 'image/background_easy.png')
            self.interface = Interface('image/interface_easy.png', 0, 520, SCREEN_WIDTH, 200, self.soldiers, self.towers)
        else: #困難模式
            self.background = Background( 0, 0, SCREEN_WIDTH ,SCREEN_HEIGHT-200, 'image/background_hard.png')
            self.interface = Interface('image/interface_hard.png', 0, 520, SCREEN_WIDTH, 200, self.soldiers, self.towers)
            self.multiplier = 2
        self.enemy_towers = EnemyTower("image/truck.png", 900, 370, 300) #敵人塔
        self.enemy_towers.hp *= self.multiplier #敵方塔數值
        self.enemy_towers.max_hp *= self.multiplier
    def generate_enemy(self):
        enemy_class = random.choice([Enemy_normal, Enemy_normal, Enemy_elite, Enemy_speed, Enemy_tank]) #隨機選擇敵人
        enemy_x = self.enemy_towers.image.rect.x - 30 #敵人生成座標
        enemy_y = self.enemy_towers.image.rect.y + self.enemy_towers.image.rect.height - 30
        enemy = enemy_class(enemy_x, enemy_y) #敵人能力數值
        enemy.hp *= 1.1**self.enemy_towers.level
        enemy.hp = int(enemy.hp)   
        enemy.max_hp *=  1.1**self.enemy_towers.level
        enemy.max_hp = int(enemy.max_hp)
        enemy.dmg *= self.multiplier* 1.1**self.enemy_towers.level
        enemy.dmg = int(enemy.dmg)
        return enemy
    def reset(self):
        self.__init__() #重置遊戲
