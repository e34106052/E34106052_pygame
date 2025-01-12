import pygame

class Background: #靜態圖片為背景
    def __init__(self, x, y, width, height, image_path):
        #設定背景座標大小
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))  
    def draw(self, screen): #畫出背景
        screen.blit(self.image, self.rect) 
        
class Button(Background): #可互動的圖片為按鈕
    def __init__(self, x, y, width, height, image_path):
        super().__init__(x, y, width, height, image_path)
    def is_clicked(self, pos): #檢查按鈕是否被點擊  
        return self.rect.collidepoint(pos)
