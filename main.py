import pygame
from mapa import Mapa
import constantes

pygame.init()

#Tela
tela = pygame.display.set_mode((constantes.LARGURA_TELA, constantes.ALTURA_TELA))
pygame.display.set_caption("Projeto Final POO")

clock = pygame.time.Clock()

#Cria o objeto Mapa
mapa = Mapa()

#Loop para o jogo
jogo_aberto = True
while jogo_aberto:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_aberto = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posição = pygame.mouse.get_pos()
            cord_x = posição[0]
            cord_y = posição[1]
            mapa.processar_click(cord_x, cord_y)

    tela.fill(constantes.AZUL)
    mapa.desenhar(tela)
    pygame.display.update()
    clock.tick(30)

pygame.quit()


