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
        dinheiro_log = DatabaseJSON("usuariologado.json")
        with open('usuariologado.json', 'r', encoding='utf-8') as f1:
            pessoa = json.load(f1)  
        with open('usuariosmoney.json', 'r', encoding='utf-8') as f2:
            salarios = json.load(f2) 
        nome1 = pessoa["nome"]
        dinheiro_pessoa = pessoa["dinheiro"]
        if nome1 in salarios:
            dinheiro_salario = salarios[nome1]
            if dinheiro_pessoa > dinheiro_salario:
                salarios[nome1] = dinheiro_pessoa
                with open('usuariosmoney.json', 'w', encoding='utf-8') as f2:
                    json.dump(salarios, f2, indent=2, ensure_ascii=False)
        else:
            salarios[nome1] = dinheiro_pessoa
            logado = DatabaseJSON("usuariosmoney.json")
            log = logado.alterar(nome1, dinheiro_pessoa )

        cidade = Cidade()
        dinheiro_atual = cidade.get_dinheiro()
        logado = dinheiro_log.alterar("dinheiro", dinheiro_atual)
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
