import pygame

class CollisionManager:
    def __init__(self, interface):
        self.interface = interface
    def bullet_enemy_collision(self, tower, enemies): #子彈擊中敵人
        for bullet in tower.bullets:
            enemy_hit = pygame.sprite.spritecollide(bullet, enemies, False)
            if enemy_hit:
                for enemy in enemy_hit:
                    bullet.kill() #子彈消失
                    enemy.hp -= tower.attack_power #敵人扣血
                    pygame.mixer.Sound("audio/attack.mp3").play() #播放音效
    def soldier_enemy_collision(self, soldiers, enemies):
        for soldier in soldiers: #單位碰撞則互相攻擊
            for enemy in enemies:
                if soldier.rect.colliderect(enemy.rect): 
                    soldier.take_damage(enemy.dmg)
                    enemy.take_damage(soldier.dmg)
    def unit_tower_collision(self, units, tower):
        for unit in units:
            if unit.rect.colliderect(tower.image.rect): #單位及塔碰撞
                tower.hp -= unit.dmg      #塔扣血
                unit.hp = 0         #單位死亡
                if tower.hp <= 0:    #塔的血量不為負值
                    tower.hp = 0
    def unit_die(self,soldiers,enemies): #單位死亡
        for soldier in soldiers:
            if soldier.hp <= 0: 
                soldier.kill()
        for enemy in enemies:
            if enemy.hp <= 0: 
                enemy.kill()
                self.interface.money+=enemy.value #敵人死亡獲得金錢