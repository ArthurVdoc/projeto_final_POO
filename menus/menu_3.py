# botao_sair.py
import pygame
import json
import sys
import constantes
import subprocess
from utilidades.botao import Botao
from menus.menu import Menu
from DatabaseJSON import DatabaseJSON
from back_entidades.cidade import Cidade

class Menu_sair(Menu):
    def __init__(self, tela, cidade: Cidade):
        self.tela = tela
        self.botao = self._criar_botao()
        self.cidade = cidade    

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
    
    def _fechar_jogo(self,arquivo_novo):

        usuario_logado = DatabaseJSON("usuariologado.json")
        usuario_rank = DatabaseJSON("usuariosmoney.json")

        # Pega os dados do JSON como dicionário
        dados_logado = usuario_logado.extrair()
        dados_rank = usuario_rank.extrair()

        nome = dados_logado["nome"]
        dinheiro = self.cidade.get_dinheiro()

        # Atualiza o dinheiro no JSON do usuário logado
        dados_logado["dinheiro"] = dinheiro
        usuario_logado.carregar(dados_logado)

        # Atualiza o rank se necessário
        if nome in dados_rank:
            if dinheiro > dados_rank[nome]:
                dados_rank[nome] = dinheiro
        else:
            dados_rank[nome] = dinheiro

        usuario_rank.carregar(dados_rank)

        pygame.quit()
        subprocess.Popen([sys.executable, arquivo_novo]) 
        sys.exit()
    
    def desenhar(self):
        self.botao.desenhar(self.tela)
    
    def tratar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            return self.botao.checar_clique(evento.pos)
        return False
        import json