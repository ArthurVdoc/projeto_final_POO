import pygame
from mapa import Mapa
import constantes

pygame.init()

#Tela
tela = pygame.display.set_mode((constantes.LARGURA_TELA, constantes.ALTURA_TELA))
pygame.display.set_caption("Projeto Final POO")

mapa = Mapa(constantes.TAMANHO_MAPA, constantes.TAMANHO_BLOCO)

