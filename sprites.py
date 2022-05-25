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