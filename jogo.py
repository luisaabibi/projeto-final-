import random
import pygame

from sprites import Cogumelo, Fox
from sprites import Pedra 
from sprites import Cobra
from sprites import Fox
pygame.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Jumpy Fox')

clock = pygame.time.Clock()
FPS = 60

game= True 
posicaox=0

image = pygame.image.load('assets/img/fundo2.jpg').convert()
image=pygame.transform.scale(image, (2400, HEIGHT))

cogumelo_img= pygame.image.load('assets/img/cogumelo.png').convert_alpha()
cogumelo_img= pygame.transform.scale(cogumelo_img, (50, 50))

pedra_img = pygame.image.load('assets/img/pedra.png').convert_alpha()
pedra_img= pygame.transform.scale(pedra_img, (80, 80))

cobra_img = pygame.image.load('assets/img/cobra.png').convert_alpha()
cobra_img= pygame.transform.scale(cobra_img, (60, 60))

fox_img = pygame.image.load('assets/img/raposa.png').convert_alpha()
fox_img= pygame.transform.scale(fox_img, (200, 200))

all_sprites = pygame.sprite.Group()
all_cogumelos = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()
all_cobras= pygame.sprite.Group()


i=0
while game :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game = False 

    cogumelo = Cogumelo(cogumelo_img, posicaox + random.randint(200,1000), 385)
    all_cogumelos.add(cogumelo)
    all_sprites.add(cogumelo)
    posicaox=cogumelo.rect.x

    pedra = Pedra(pedra_img, posicaox + random.randint(200,800), 370)
    all_pedras.add(pedra)
    all_sprites.add(pedra)

    posicaox=pedra.rect.x

    cobra = Cobra(cobra_img, posicaox + random.randint(200,1000), 385)
    all_pedras.add(cobra)
    all_sprites.add(cobra)

    posicaox=cobra.rect.x


    fox = Fox(fox_img, 150, 295)
    all_sprites.add(fox)


    

    all_sprites.update()

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (i, 0))

    if i == -WIDTH:
        i=0
    else:
        i-=5

    all_sprites.draw(window)
    pygame.display.update()



    
player = Fox()

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_SPACE:
                player.speedy -= 10

        if event.type == pygame.KEYUP:
        
            if event.key == pygame.K_SPACE:
                player.speedy += 10 
        


pygame.quit()