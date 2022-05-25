import py
import pygame 
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


i=0

while game :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game = False 

    window.fill((0, 0, 0))  # Preenche com a cor branca]


    window.blit(image, (i, 0))

    if i == -1200:
        i=0
    else:
        i-=5
    pygame.display.update()

pygame.quit()
