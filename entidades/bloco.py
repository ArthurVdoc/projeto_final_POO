import pygame
import constantes

class Bloco:
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.tamanho = constantes.TAMANHO_BLOCO
        self.tem_construção = False

    def desenhar(self, tela):
        if self.tem_construção:
            cor = constantes.MARROM
        else:
            cor = constantes.VERDE
        retangulo = pygame.Rect(self.cord_x*self.tamanho, self.cord_y*self.tamanho, self.tamanho, self.tamanho)
        pygame.draw.rect(tela, cor, retangulo)
        pygame.draw.rect(tela, constantes.PRETO, retangulo, 1)
    
    def click(self):
        print(f"Alterou a cor do bloco ({self.cord_x}, {self.cord_y})")
        self.tem_construção = not self.tem_construção





