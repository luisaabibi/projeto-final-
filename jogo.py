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

while jogo:
    window.blit(imagem_inicial, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
            game = False
        if event.type == pygame.KEYDOWN:
            jogo = False

    pygame.display.update()

# Loop principal
while game:
    clock.tick(FPS)
    fox.rect.y == 295
    fox.speedy = 0
    all_sprites.add(fox)

    # Pega o valor do tempo
    tempo = pygame.time.get_ticks()

    # verifica as ações do player
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE] and not fox.dino_pulando:
        fox.dino_padrao = False
        fox.dino_pulando = True
        fox.v_jump = 9
    elif not (fox.dino_pulando):
        fox.dino_padrao = True
        fox.dino_pulando = False


    if tempo % 30 == 0:
            cogumelo = Cogumelo(cogumelo_img, posicaox + random.randint(200, 1000), 385)
            all_cogumelos.add(cogumelo)
            all_sprites.add(cogumelo)
            posicaox = cogumelo.rect.x

        if tempo % 60 == 0:
            pedra = Pedra(pedra_img, posicaox + random.randint(200, 800), 370)
            all_pedras.add(pedra)
            all_sprites.add(pedra)
            posicaox = pedra.rect.x

        if tempo % 90 == 0:
            cobra = Cobra(cobra_img, posicaox + random.randint(200, 1000), 385)
            all_pedras.add(cobra)
            all_sprites.add(cobra)
            posicaox = cobra.rect.x

        if i == -WIDTH:
            i = 0
        else:
            i -= 5

        all_sprites.update()




        






























































































