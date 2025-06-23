import pygame
import constantes

class Dinheiro:
    def __init__(self, dinheiro_inicial: int):
        self._dinheiro = dinheiro_inicial
        self.fonte = pygame.font.SysFont(None, 24)


    @property
    def dinheiro(self):
        return self._dinheiro
    
    def gastar(self, valor: int):
        if self._dinheiro >= valor:
            self._dinheiro -= valor
            return True
        return False
    
    def receber(self, valor: int):
        self._dinheiro += valor
    
    def desenhar(self, tela: pygame.display):
        texto = "Dinheiro: $" + str(self._dinheiro)
        texto_render = self.fonte.render(texto, True, constantes.AMARELO)
        tela.blit(texto_render, (10, 10)) 

    