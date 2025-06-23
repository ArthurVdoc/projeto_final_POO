from front_entidades.bloco import Bloco
import constantes
import pygame

class Mapa:
    def __init__(self):
        self.tamanho = constantes.TAMANHO_MAPA
        self.blocos = []

        for y in range(constantes.TAMANHO_MAPA):
            linha = []
            for x in range(constantes.TAMANHO_MAPA):
                bloco = Bloco(x, y)
                linha.append(bloco)
            self.blocos.append(linha)
    
    def desenhar(self, tela: pygame.display):
        for linha in self.blocos:
            for bloco in linha:
                bloco.desenhar(tela)
    
    def obter_bloco(self, pixel_x: int, pixel_y: int):
        linha = pixel_y // constantes.TAMANHO_BLOCO
        coluna = pixel_x // constantes.TAMANHO_BLOCO
        if 0 <= linha < self.tamanho and 0 <= coluna < self.tamanho:
            return self.blocos[linha][coluna]
        return None