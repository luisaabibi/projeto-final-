from time import clock_gettime
import pygame
import py 

clock_gettime


score_value=0
font=pygame.font.Font('ADELIA.otf',32)
textX = 10
testy = 10
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))



show_score(textX,testy)