import random
import py
import pygame

from sprites import Cogumelo 
pygame.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Jumpy Fox')

clock = pygame.time.Clock()
FPS = 30

game= True 

image = pygame.image.load('assets/img/fundo2.jpg').convert()
image=pygame.transform.scale(image, (2400, HEIGHT))

cogumelo_img= pygame.image.load('assets/img/cogumelo.png').convert_alpha()
cogumelo_img= pygame.transform.scale(cogumelo_img, (40, 40))

all_sprites = pygame.sprite.Group()
all_cogumelos = pygame.sprite.Group()

i=0
while game :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game = False 


    if len(all_cogumelos) < 10:
        cogumelo = Cogumelo(cogumelo_img, WIDTH + random.randint(0, 2400), 400)
        all_cogumelos.add(cogumelo)
        all_sprites.add(cogumelo)


    all_sprites.update()

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (i, 0))

    if i == -WIDTH:
        i=0
    else:
        i-=5

    all_sprites.draw(window)
    pygame.display.update()
player = "(img.fox)"
while game:
    clock.tick(FPS)

    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
       
        if event.type == pygame.KEYUP:
           
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8


pygame.quit()