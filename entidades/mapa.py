from bloco import Bloco
import constantes

class Mapa:
    def __init__(self):
        self.tamanho = constantes.TAMANHO_MAPA
        self.blocos = []

        for y in range(constantes.TAMANHO_MAPA):
            linha = []
            for x in range(constantes.TAMANHO_MAPA):
                bloco = Bloco(x, y)
                linha.append(bloco)
            self.blocos.append(linha)
    
    def desenhar(self, tela):
        for linha in self.blocos:
            for bloco in linha:
                bloco.desenhar(tela)
    
    def processar_click(self, cord_x, cord_y):
        linha = cord_y // constantes.TAMANHO_BLOCO
        coluna = cord_x // constantes.TAMANHO_BLOCO
        if 0 <= linha and linha < self.tamanho and 0 <= coluna and coluna < self.tamanho:
            self.blocos[linha][coluna].click()