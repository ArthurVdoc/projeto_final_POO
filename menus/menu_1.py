from menus.menu import Menu
from utilidades.botao import Botao
from entidades.bloco import Bloco
import constantes

import pygame

class Menu_1(Menu):
    def __init__(self, bloco, posição_mouse, abrir_menu_2):
        self.bloco = bloco
        self.posição_mouse = posição_mouse
        self.botoes = []
        self.abrir_menu_2 = abrir_menu_2
        self.criar_botoes()
    
    def criar_botoes(self):
        x, y = self.posição_mouse
        largura  = constantes.LARGURA_BT1
        altura = constantes.ALTURA_BT1
        espaço = constantes.espaço_BT1

        self.botoes.append(Botao("Adicionar Construção", x, y, 
                                 largura, altura, 
                                 lambda: self.abrir_menu_2("construção", self.bloco, 
                                                           x+largura+espaço, y)))
        self.botoes.append(Botao("adicionar Morador", x, y+altura+espaço, 
                                 largura, altura, 
                                 lambda: self.abrir_menu_2("morador", self.bloco, 
                                                           x+largura+espaço, y)))
    
    def desenhar(self, tela):
        for botao in self.botoes:
            botao.desenhar(tela)

    def tratar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posição = evento.pos
            for botao in self.botoes:
                botao.checar_clique(posição)