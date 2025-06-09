from menus.menu import Menu
from utilidades.botao import Botao
from entidades.bloco import Bloco
import constantes

import pygame

class Menu_1(Menu):
    def __init__(self, bloco, ao_fechar):
        self.bloco = bloco
        self.botoes = []
        self.ao_fechar = ao_fechar
        self.criar_botoes()
    
    def criar_botoes(self):
        x = self.bloco.cord_x * self.bloco.tamanho
        y = self.bloco.cord_y * self.bloco.tamanho
        largura  = constantes.LARGURA_BT1
        altura = constantes.ALTURA_BT1
        espaço = constantes.espaço_BT1

        self.botoes.append(Botao("Adicionar Construção", x, y, largura, altura, self.adicionar_construção))
        self.botoes.append(Botao("adicionar Morador", x, y+altura+espaço, largura, altura, self.adicionar_morador))
    
    def adicionar_construção(self):
        self.bloco.definir_estado(constantes.CONSTRUÇÃO)
        self.ao_fechar()

    def adicionar_morador(self):
        self.bloco.definir_estado(constantes.MORADOR)
        self.ao_fechar()
    
    def desenhar(self, tela):
        for botao in self.botoes:
            botao.desenhar(tela)

    def tratar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posição = evento.pos
            for botao in self.botoes:
                botao.checar_clique(posição)