from entidades.mapa import Mapa
from menus.menu_1 import Menu_1
import constantes

import pygame

class Jogo:
    def __init__(self):
        #inicia o pygame
        pygame.init()
        #cria a tela
        self.tela = pygame.display.set_mode((constantes.LARGURA_TELA, constantes.ALTURA_TELA))
        pygame.display.set_caption("Projeto Final POO")
        #cria o clock temporal
        self.clock = pygame.time.Clock()
        #cria o mapa
        self.mapa = Mapa()

        self.menu_1_ativo = None
        self.jogo_ativo = True
    
    def executar(self):
        while self.jogo_ativo:
            self.tratar_eventos()
            self.desenhar()
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jogo_ativo = False
            elif self.menu_1_ativo:
                self.menu_1_ativo.tratar_evento(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                bloco = self.mapa.obter_bloco(evento.pos[0], evento.pos[1])
                if bloco:
                    self.menu_1_ativo = Menu_1(bloco, evento.pos, self.fechar_menu)
    
    def fechar_menu(self):
        self.menu_1_ativo = None

    def desenhar(self):
        self.tela.fill(constantes.AZUL)
        self.mapa.desenhar(self.tela)
        if self.menu_1_ativo:
            self.menu_1_ativo.desenhar(self.tela)