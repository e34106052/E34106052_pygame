from setting import *
from collision_manager import CollisionManager

class GameControl:
    def __init__(self, model):
        self.model = model 
        self.collision_manager = CollisionManager(model.interface) # 初始化碰撞管理
        self.enemy_tower_delay = 40000 #敵方升級時間
        self.tower_time = 0 
        self.enemy_generator_delay = 5000 #敵方士兵生成時間
        self.enemy_time = 0
        self.global_time = 0 #全局遊戲時間
        self.start_time = pygame.time.get_ticks()
        self.timer_running = False #一開始不計時
    def update_global_time(self):
        if self.timer_running: #計時器運行中
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.start_time
            self.global_time += elapsed_time
            self.start_time = current_time
    def toggle_timer(self):
        if self.timer_running: #暫停計時
            self.timer_running = False
            self.global_time += pygame.time.get_ticks() - self.start_time
        else:
            self.timer_running = True #繼續計時
            self.start_time = pygame.time.get_ticks()
    def enemy_generator(self): #敵方士兵生成
        if self.global_time - self.enemy_time > self.enemy_generator_delay:
            enemy = self.model.generate_enemy()
            self.model.enemies.add(enemy)
            self.enemy_time = self.global_time
    def update_enemy_tower(self): #敵方塔升級
        if self.global_time - self.tower_time > self.enemy_tower_delay:
            self.model.enemy_towers.upgrade()
            self.tower_time = self.global_time
    def check_for_collisions(self): #碰撞檢測
        self.collision_manager.bullet_enemy_collision(self.model.towers, self.model.enemies)
        self.collision_manager.soldier_enemy_collision(self.model.soldiers, self.model.enemies)
        self.collision_manager.unit_tower_collision(self.model.soldiers, self.model.enemy_towers)
        self.collision_manager.unit_tower_collision(self.model.enemies, self.model.towers)
        self.collision_manager.unit_die(self.model.soldiers, self.model.enemies)
    def update(self, game_state):
        if game_state == GAME_RUNNING:
            if not self.timer_running:  # 啟動計時器
                self.timer_running = True
                self.start_time = pygame.time.get_ticks()  # 重置起始時間
            self.update_global_time()
            self.model.towers.update()
            self.model.enemy_towers.update()
            self.model.soldiers.update()
            self.model.enemies.update()
            self.enemy_generator()
            self.update_enemy_tower()
            self.check_for_collisions()
            if self.model.towers.hp <= 0 or self.model.enemy_towers.hp <= 0: # 遊戲結束條件
                return GAME_OVER
        return game_state

