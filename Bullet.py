import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,gun):
        #Создаем пулю в позии пушки
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 139,195,74
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #Перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        #РИсуем пульку на экране
        pygame.draw.rect(self.screen,self.color,self.rect)