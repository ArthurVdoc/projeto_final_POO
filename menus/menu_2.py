from menus.menu import Menu
from utilidades.botao import Botao
from front_entidades.bloco import Bloco
import constantes

import pygame


class Menu_2(Menu):
    def __init__(self, tipo, bloco, cord_x, cord_y, ao_fechar, cidade):
        self.tipo = tipo
        self.bloco = bloco
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.botoes = []
        self.ao_fechar  = ao_fechar
        self.criar_botoes()
        self.cidade = cidade
    
    def criar_botoes(self):
        largura = constantes.LARGURA_BT2
        altura = constantes.ALTURA_BT2
        espaço = constantes.espaço_BT2
        if self.tipo == "construção":
            self.botoes.append(Botao("Casa", self.cord_x, self.cord_y, 
                                     largura, altura, 
                                     lambda: self.definir_estado(self.bloco, constantes.CASA)))
            self.botoes.append(Botao("Taverna", self.cord_x, self.cord_y + altura + espaço, 
                                     largura, altura, 
                                     lambda: self.definir_estado(self.bloco, constantes.TAVERNA)))
            self.botoes.append(Botao("Caminho", self.cord_x, self.cord_y + (altura*2) + espaço, 
                                     largura, altura, 
                                     lambda: self.definir_estado(self.bloco, constantes.CAMINHO)))
                  
        elif self.tipo == "morador":
            self.botoes.append(Botao("Fazendeiro", self.cord_x, self.cord_y, 
                                     largura, altura,
                                     lambda: self.definir_estado(self.bloco, constantes.FAZENDEIRO)))
            self.botoes.append(Botao("Caçador", self.cord_x, self.cord_y + altura + espaço, 
                                     largura, altura, 
                                     lambda: self.definir_estado(self.bloco, constantes.CAÇADOR)))    
    
    def definir_estado(self, bloco, estado):
        if estado in (constantes.CASA, constantes.TAVERNA, constantes.CAMINHO):
            if self.cidade.adicionar_construção(estado):
                bloco.definir_estado(estado)
        elif estado in (constantes.FAZENDEIRO, constantes.CAÇADOR):
            if self.cidade.adicionar_morador(estado):
                bloco.definir_estado(estado)
        self.ao_fechar()
    
    def desenhar(self, tela):
        for botao in self.botoes:
            botao.desenhar(tela)

    def tratar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posição = evento.pos
            clique_em_botao = False
            
            # Verifica se clicou em algum botão
            for botao in self.botoes:
                if botao.checar_clique(posição):
                    clique_em_botao = True
                    break
            
            # Se não clicou em nenhum botão, fecha o menu
            if not clique_em_botao:
                self.ao_fechar()