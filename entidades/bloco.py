import pygame
import constantes

class Bloco:
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.tamanho = constantes.TAMANHO_BLOCO
        self.estado = constantes.VAZIO

    def desenhar(self, tela):
        if self.estado == constantes.CONSTRUÇÃO:
            cor = constantes.MARROM
        elif self.estado == constantes.MORADOR:
            cor = constantes.AZUL
        else:
            cor = constantes.VERDE
        retangulo = pygame.Rect(self.cord_x*self.tamanho, self.cord_y*self.tamanho, self.tamanho, self.tamanho)
        pygame.draw.rect(tela, cor, retangulo)
        pygame.draw.rect(tela, constantes.PRETO, retangulo, 1)
    
    def definir_estado(self, novo_estado):
        self.estado = novo_estado




