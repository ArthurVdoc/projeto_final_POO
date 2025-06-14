from back_entidades.moradores.morador_base import Morador

class Fazendeiro(Morador):
    def custo(self):
        return 100
    def rendimento_dia(self):
        return 20
    
class Cacador(Morador):
    def custo(self):
        return 200
    def rendimento_dia(self):
        return 40
