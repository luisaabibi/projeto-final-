import py
import pygame 
pygame.init()

WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Jumpy Fox')

clock = pygame.time.Clock()
FPS = 30

game= True 

image = pygame.image.load().convert()



while game :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game = False 

    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
