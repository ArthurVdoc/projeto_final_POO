from back_entidades.construcoes.construcao_base import Construção

class Casa(Construção):
    def custo(self):
        return 100
    
class Taverna(Construção):
    def custo(self):
        return 300