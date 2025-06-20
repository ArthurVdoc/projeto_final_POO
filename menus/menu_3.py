# botao_sair.py
import pygame
import sys
import constantes
import subprocess
from utilidades.botao import Botao

class Menu_sair:
    def __init__(self, tela):
        self.tela = tela
        self.botao = self._criar_botao()
    
    def _criar_botao(self):
        x = constantes.LARGURA_TELA - constantes.LARGURA_BT1 - 10
        y = 10
        return Botao(
            "Sair",
            x, y,
            constantes.LARGURA_BT1,
            constantes.ALTURA_BT1,
            lambda: self._fechar_jogo("Login.py")
        )
    
    def _fechar_jogo(self, arquivo_novo):
        pygame.quit()
        subprocess.Popen([sys.executable, arquivo_novo]) 
        sys.exit()
    
    def desenhar(self):
        self.botao.desenhar(self.tela)
    
    def tratar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            return self.botao.checar_clique(evento.pos)
        return False