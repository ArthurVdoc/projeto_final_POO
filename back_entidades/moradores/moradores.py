from back_entidades.moradores.morador_base import Morador

#Cria a classe Fazendeiro, um dos tipos de morador, herda da classe Morador
class Fazendeiro(Morador):
    #Determina que o custo para se ter um fazendeiro é de 100 reais.
    def custo(self)-> int:
        return 100
    #Determina que o fazendeiro rende 20 reais por dia.
    def rendimento_dia(self) -> int:
        return 20
    
class Cacador(Morador):
    #Determina que o custo para se ter um caçador é de 200 reais.
    def custo(self) -> int:
        return 200
    #Determina que o fazendeiro rende 20 reais por dia.
    def rendimento_dia(self) -> int:
        return 40
