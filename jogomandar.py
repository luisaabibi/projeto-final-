import random
from tkinter.tix import Tree
import pygame
import time
from sprites import Cogumelo, Fox
from sprites import Pedra
from sprites import Cobra
from sprites import Fox


pygame.init()

# Largura e altura da tela
WIDTH = 1200
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Define nome da janela e icone
pygame.display.set_caption("Jumpy Fox")
icone = pygame.image.load("./Assets/img/raposa.png")
pygame.display.set_icon(icone)

clock = pygame.time.Clock()
FPS = 60

# Define loop principal, posicao inicial, pontos iniciais e carrega fonte
game = True
jogo = True
pontos = 0
posicaox = 0
fonte = pygame.font.SysFont("comicsans", 30, True)

# carrega e inicia a musica
pygame.mixer.music.load('assets\som\som_crash_bandicoot.mp3')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(loops=-1)

# Carrega imagens da raposa + obtaculos
image = pygame.image.load("assets/img/fundo2.jpg").convert()
image = pygame.transform.scale(image, (2400, HEIGHT))
imagem_inicial = pygame.image.load("assets/img/fundoinicio.png").convert_alpha()
imagem_inicial = pygame.transform.scale(imagem_inicial, (WIDTH, HEIGHT))
game_over = pygame.image.load("assets/img/game over.png")
game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))


cogumelo_img = pygame.image.load("assets/img/cogumelo.png").convert_alpha()
cogumelo_img = pygame.transform.scale(cogumelo_img, (50, 50))

pedra_img = pygame.image.load("assets/img/pedra.png").convert_alpha()
pedra_img = pygame.transform.scale(pedra_img, (80, 80))

cobra_img = pygame.image.load("assets/img/cobra.png").convert_alpha()
cobra_img = pygame.transform.scale(cobra_img, (60, 60))

fox_img = pygame.image.load("assets/img/raposa.png").convert_alpha()
fox_img = pygame.transform.scale(fox_img, (200, 200))

all_sprites = pygame.sprite.Group()
all_cogumelos = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()
all_cobras = pygame.sprite.Group()
fox = Fox(fox_img, 150, 295)
i = 0

# gera os primeiros obstáculos
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

#Tela Inicial
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
    if teclas[pygame.K_SPACE] and not fox.fox_pulando:
        fox.fox_padrao = False
        fox.fox_pulando = True
        fox.v_jump = 9
    elif not (fox.fox_pulando):
        fox.fox_padrao = True
        fox.fox_pulando = False

    # Gera os obstáculos conforme o passar do tempo
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

    # Preenche com a cor branca
    window.fill((0, 0, 0))

    window.blit(image, (i, 0))

    # Define as colisões entre o player e os obstáculos
    colisao_cogumelo = pygame.sprite.spritecollide(
        fox, all_cogumelos, True, pygame.sprite.collide_mask
    )
    colisao_pedra = pygame.sprite.spritecollide(
        fox, all_pedras, True, pygame.sprite.collide_mask
    )
    colisao_cobra = pygame.sprite.spritecollide(
        fox, all_cobras, True, pygame.sprite.collide_mask
    )

    # Verifica as colisões
    if colisao_pedra:
        time.sleep(0.2)
        window.blit(game_over,(0,0))
        text = fonte.render("pontuação final: " + str(pontos), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (580, 400)
        window.blit(text, textRect)
        pygame.display.update()
        time.sleep(3.0)
        game = False

    if colisao_cogumelo:
        time.sleep(0.2)
        window.blit(game_over,(0,0))
        text = fonte.render("pontuação final: " + str(pontos), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (580, 400)
        window.blit(text, textRect)
        pygame.display.update()
        time.sleep(3.0)
        game = False

    if colisao_cobra:
        time.sleep(0.2)
        window.blit(game_over,(0,0))
        text = fonte.render("pontuação final: " + str(pontos), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (580, 400)
        window.blit(text, textRect)
        pygame.display.update()
        time.sleep(3.0)
        game = False
    all_sprites.draw(window)

    # Atualiza os pontos
    pontos += 10
    text = fonte.render("pontos: " + str(pontos), False, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 40)
    window.blit(text, textRect)

    # Imprime a pontuação no terminal
    if game == False:
        print(f"Sua pontuação foi de {pontos}")
    pygame.display.update()
