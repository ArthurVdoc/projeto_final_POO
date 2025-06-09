import pygame
import constantes 

class Botao:
    def __init__(self, texto, cord_x, cord_y, largura, altura, funcao_retoro):
        self.texto = texto
        self.retangulo = pygame.Rect(cord_x, cord_y, largura, altura)
        self.retorno = funcao_retoro
        self.fonte = pygame.font.SysFont(None, 24)
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, constantes.CINZA, self.retangulo)
        pygame.draw.rect(tela, constantes.PRETO, self.retangulo, 1)

        texto_render = self.fonte.render(self.texto, True, constantes.PRETO)
        texto_centro = texto_render.get_rect(center=self.retangulo.center)
        tela.blit(texto_render, texto_centro)
    
    def checar_clique(self, posicao):
        if self.retangulo.collidepoint(posicao):
            self.retorno()