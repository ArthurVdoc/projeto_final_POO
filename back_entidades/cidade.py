from back_entidades.construcoes.construcoes import Casa, Taverna
from back_entidades.moradores.moradores import Fazendeiro, Cacador
from back_entidades.deinheiro import Dinheiro
from back_entidades.tempo import Tempo

class Cidade:
    def __init__(self):
        self.dinheiro = Dinheiro(500)
        self.tempo = Tempo()
        self.ultimo_dia = 0
        self.construções = []
        self.moradores = []

    def adicionar_construção(self, construção):
        if self.dinheiro.gastar(construção.custo()):
            self.construções.append(construção)
            return True
        return False