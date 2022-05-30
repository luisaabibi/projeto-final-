import pygame

class Cogumelo(pygame.sprite.Sprite):
    def _init_(self, img, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -5

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < -50:
            self.kill()

class Pedra(pygame.sprite.Sprite):
    def _init_(self, img, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -5
    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < -50:
            self.kill()

class Cobra(pygame.sprite.Sprite):
    def _init_(self, img, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -5
    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < -50:
            self.kill()



class Fox(pygame.sprite.Sprite):
    def _init_(self, assets, x, y):
        pygame.sprite.Sprite._init_(self)
        self.image = assets['raposa2']
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 40
        self.speedx = 0

