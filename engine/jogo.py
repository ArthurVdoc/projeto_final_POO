from utilidades.carregar_sprites import CarregarSprites
from front_entidades.mapa import Mapa
from menus.menu_1 import Menu_1
from menus.menu_2 import Menu_2
from menus.menu_3 import Menu_sair
from back_entidades.cidade import Cidade
import constantes
import os
import pygame

class Jogo:
    def __init__(self):
        #inicia o pygame
        pygame.init()
        #cria a tela
        self.tela = pygame.display.set_mode((constantes.LARGURA_TELA, 
                                             constantes.ALTURA_TELA))
        pygame.display.set_caption("Projeto Final POO")
        #carrega as sprites
        CarregarSprites.carregar_sprites()
        #cria o clock temporal
        self.clock = pygame.time.Clock()
        #cria o mapa
        self.mapa = Mapa()
        #cria a logica de cidade
        self.cidade = Cidade()
        self.botao_sair = Menu_sair(self.tela,self.cidade)
        self.menu_1_ativo = None
        self.menu_2_ativo = None
        self.jogo_ativo = True
    
    def executar(self):
        while self.jogo_ativo:
            self.tratar_eventos()
            self.cidade.atualizar_dinheiro_diario()
            self.desenhar()
            pygame.display.update()

            self.limpar_terminal()
            print("Dinheiro: ", self.cidade.dinheiro.dinheiro)

            self.clock.tick(30)
        pygame.quit()

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jogo_ativo = False
            elif self.botao_sair.tratar_evento(evento):
                continue 
            elif self.menu_2_ativo:
                self.menu_2_ativo.tratar_evento(evento)
            elif self.menu_1_ativo:
                 self.menu_1_ativo.tratar_evento(evento) 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                bloco = self.mapa.obter_bloco(evento.pos[0], evento.pos[1])
                if bloco:
                    self.menu_1_ativo = Menu_1(bloco, evento.pos, self.abrir_menu_2, self.fechar_menus)##
    
    def abrir_menu_2(self, tipo: str, bloco: int , x: int, y: int):
        self.menu_2_ativo = Menu_2(tipo, bloco, x, y, self.fechar_menus, self.cidade)

    def fechar_menus(self):
        self.menu_1_ativo = None
        self.menu_2_ativo = None

    def desenhar(self):
        self.tela.fill(constantes.AZUL)
        self.mapa.desenhar(self.tela)
        self.cidade.dinheiro.desenhar(self.tela)
        if self.menu_1_ativo:
            self.menu_1_ativo.desenhar(self.tela)
        if self.menu_2_ativo:
            self.menu_2_ativo.desenhar(self.tela)

        if not self.menu_1_ativo and not self.menu_2_ativo:
            self.botao_sair.desenhar()
    
    def limpar_terminal(self):
        os.system('clear')
