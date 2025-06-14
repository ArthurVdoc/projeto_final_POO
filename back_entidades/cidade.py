from back_entidades.construcoes.construcoes import Casa, Taverna
from back_entidades.moradores.moradores import Fazendeiro, Cacador
from back_entidades.deinheiro import Dinheiro
from back_entidades.tempo import Tempo
import constantes

class Cidade:
    def __init__(self):
        self.dinheiro = Dinheiro(1000)
        self.tempo = Tempo()
        self.ultimo_dia = 0
        self.construções = []
        self.moradores = []

    def adicionar_construção(self, estado):
        if estado == constantes.CASA:
            construção = Casa()
        elif estado == constantes.TAVERNA:
            construção = Taverna()
        elif estado == constantes.CAMINHO:
            return True
        else:
            return False
            
        if self.dinheiro.gastar(construção.custo()):
            self.construções.append(construção)
            #print ("Dinheiro atual: ", self.dinheiro.dinheiro,
            #       "\nConstruções: ", self.construções, 
            #       "\nMoradores: ", self.moradores)
            return True
        return False
    
    def adicionar_morador(self, estado):
        if estado == constantes.FAZENDEIRO:
            morador = Fazendeiro()
        elif estado == constantes.CAÇADOR:
            morador = Cacador()
        else:
            return False

        casas_disponiveis = sum(1 for c in self.construções if isinstance(c, Casa))
        if len(self.moradores) < casas_disponiveis:
            if self.dinheiro.gastar(morador.custo()):
                self.moradores.append(morador)
                #print ("Dinheiro atual: ", self.dinheiro.dinheiro, 
                #       "\nConstruções: ", self.construções, 
                #       "\nMoradores: ", self.moradores, 
                #       "\n", self.tempo.dias_passados())
                return True
        return False   

    def atualizar_dinheiro_diario(self):
        dia_atual = self.tempo.dias_passados()
        if dia_atual > self.ultimo_dia:
            dias_passados = dia_atual - self.ultimo_dia
            for i in range(dias_passados):
                recebimento = sum(m.rendimento_dia() for m in self.moradores)
                multiplicador = 1 + sum(0.2 for t in self.construções if isinstance(t, Taverna))
                recebimento = recebimento*multiplicador
                self.dinheiro.receber(recebimento) 
            self.ultimo_dia = dia_atual
    
    def get_dinheiro(self):
        return self.dinheiro.dinheiro
        
