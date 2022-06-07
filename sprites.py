import pygame

class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
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
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
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
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
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
    x = 150
    y = 295
    
    def __init__(self, img,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.fox_padrao = True
        self.fox_pulando = False

        self.step_index = 0
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.fox_pulando:
            self.pular()
    def pular(self):
        self.rect.y -= 10
        if self.fox_pulando:
            self.rect.y -= self.v_jump * 3
            self.v_jump -= 0.8
        if self.rect.y >= self.y:
            self.fox_pulando = False
            self.rect.y = self.y

       

       