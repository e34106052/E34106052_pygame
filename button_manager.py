from unit import Soldier
import pygame

class SummonManager:
    def __init__(self, soldiers, player_tower, summon_cost=50, soldier = Soldier):
        self.soldiers = soldiers #士兵群組
        self.player_tower = player_tower #我方塔
        self.summon_cost = summon_cost #按下按鈕的花費
        self.soldier = soldier #士兵類別
    def summon_soldier(self, money):
        if money >= self.summon_cost: # 檢查金錢足夠
            #召喚士兵的座標
            soldier_x = self.player_tower.image.rect.x + self.player_tower.image.rect.width 
            soldier_y = self.player_tower.image.rect.y + self.player_tower.image.rect.height - 30
            soldier_lv = self.soldier(soldier_x, soldier_y) #士兵能力素質
            #血量、攻擊力隨著塔等級提升
            soldier_lv.hp *= 1.1**self.player_tower.level 
            soldier_lv.hp = int(soldier_lv.hp)
            soldier_lv.max_hp *= 1.1**self.player_tower.level
            soldier_lv.max_hp = int(soldier_lv.max_hp)
            soldier_lv.dmg *= 1.1**self.player_tower.level
            soldier_lv.dmg = int(soldier_lv.dmg)
            self.soldiers.add(soldier_lv)  # 加入士兵群組
            return self.summon_cost  # 扣除金錢
        return 0  # 金錢不足，不扣錢 
class UpgradeManager:
    def __init__(self, player_tower, upgrade_health_cost = 300, upgrade_cannon_cost = 400):
        self.player_tower = player_tower #我方塔
        self.upgrade_health_cost = upgrade_health_cost #升級血量的花費
        self.upgrade_cannon_cost = upgrade_cannon_cost #升級炮台的花費
        self.sound = pygame.mixer.Sound("audio/upgrade.mp3") #升級音效
    def upgrade_health(self, money): #對塔進行升級
        if money >= self.upgrade_health_cost:   # 金錢足夠
            self.player_tower.upgrade_health()  #升級血量
            self.sound.play().set_volume(0.2)   #播放音效
            return self.upgrade_health_cost  # 扣除金錢
        return 0  # 金錢不足，不扣錢
    def upgrade_cannon(self, money): #對砲台進行升級
        if money >= self.upgrade_cannon_cost:  # 金錢足夠
            self.player_tower.upgrade_cannon()  #升級砲台
            self.sound.play().set_volume(0.2) #撥放音效
            return self.upgrade_cannon_cost  # 扣除金錢
        return 0  # 金錢不足，不扣錢