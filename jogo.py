import random
from tkinter.tix import Tree
import pygame
import time
from sprites import Cogumelo, Fox
from sprites import Pedra
from sprites import Cobra
from sprites import Fox

pygame.init()

WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Jumpy Fox")
icone = pygame.image.load("./Assets/img/raposa.png")
pygame.display.set_icon(icone)

clock = pygame.time.Clock()
FPS = 60

game = True
jogo = True
pontos = 0
posicaox = 0
fonte = pygame.font.SysFont("comicsans", 30, True)


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


imagem_inicial = pygame.image.load("assets/img/fundoinicio.png").convert_alpha()
imagem_inicial = pygame.transform.scale(imagem_inicial, (WIDTH, HEIGHT))

game_over = pygame.image.load("assets/img/gameover.png")
game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()
all_cogumelos = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()
all_cobras = pygame.sprite.Group()
fox = Fox(fox_img, 150, 295)
i = 0

cogumelo = Cogumelo(cogumelo_img, posicaox + random.randint(700, 1000), 385)
all_cogumelos.add(cogumelo)
all_sprites.add(cogumelo)
posicaox = cogumelo.rect.x

pedra = Pedra(pedra_img, posicaox + random.randint(500, 800), 370)
all_pedras.add(pedra)
all_sprites.add(pedra)
posicaox = pedra.rect.x

cobra = Cobra(cobra_img, posicaox + random.randint(700, 1000), 385)
all_pedras.add(cobra)
all_sprites.add(cobra)
posicaox = cobra.rect.x


while not crash :
    gameDisplay.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True 
        if event.type== pygame.KEYDOWN:
            start = True 
            if event.key == pygame.K_DOWN :
                slow_motion= True 
            if event.key == pygame.K_UP :
                if height >= 110 : jump= True 
        if event.type == pygame.KEYUP:
            slow_motion = False 
            if event.key == pygame.K_DOWN :
                state = run 
    





























































































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
fox = Fox(fox_img, 150, 295)
i=0

cogumelo = Cogumelo(cogumelo_img, posicaox + random.randint(200,1000), 385)
all_cogumelos.add(cogumelo)
all_sprites.add(cogumelo)
posicaox=cogumelo.rect.x

pedra = Pedra(pedra_img, posicaox + random.randint(200,800), 370)
all_pedras.add(pedra)
all_sprites.add(pedra)

posicaox=pedra.rect.x

cobra = Cobra(cobra_img, posicaox + random.randint(200,1000), 385)
all_cobras.add(cobra)
all_sprites.add(cobra)

posicaox=cobra.rect.x

obstacles = [all_pedras, all_cogumelos, all_cobras] 





while game :
    clock.tick(FPS)
    fox.rect.y == 295
    fox.speedy=0
    all_sprites.add(fox)


    '''keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        fox.speedy =- 100
        print(keys[pygame.K_SPACE])'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fox.speedy =- 100

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                fox.speedy =+ 100

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

    
    

    if i == -WIDTH:
        i=0
    else:
        i-=5
    

    all_sprites.update()

    window.fill((0, 0, 0))  # Preenche com a cor branca
    
    window.blit(image, (i, 0))
    



    all_sprites.draw(window)
    pygame.display.update()





