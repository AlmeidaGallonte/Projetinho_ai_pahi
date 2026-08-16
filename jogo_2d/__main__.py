import pygame
from random import randint
from pygame.locals import *
from sys import exit
from time import sleep

pygame.init()

largura = 640
altura = 480
x_player = largura / 2
y_player = altura / 2
vel = 5
x_moeda = randint(40,600)
y_moeda = randint(50,430)

pontos = 0

fonte = pygame.font.SysFont('arail', 20, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Lua')
relogio = pygame.time.Clock()

#loop principal 
while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    msg = f'PONTOS: {pontos}'
    txt_fort = fonte.render(msg, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x_player -= vel
    if pygame.key.get_pressed()[K_d]:
            x_player += vel
    if pygame.key.get_pressed()[K_w]:
            y_player -= vel
    if pygame.key.get_pressed()[K_s]:
            y_player += vel
                
    Player = pygame.draw.circle(tela, (200,50,10), (x_player,y_player),20)
    Moeda = pygame.draw.rect(tela, (255, 255,0), (x_moeda,y_moeda,10,10))

    if Player.colliderect(Moeda):
          x_moeda = randint(40,600)
          y_moeda = randint(50,430)
          pontos += 1
    tela.blit(txt_fort, (10, 10))
    pygame.display.update()