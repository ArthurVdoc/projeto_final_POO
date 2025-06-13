
class Dinheiro:
    def __init__(self, dinheiro_inicial):
        self._dinheiro = dinheiro_inicial

    @property
    def dinheiro(self):
        return self.__dinheiro
    
    def gastar(self, valor):
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return True
        return False
    
    def receber(self, valor):
        self.__dinheiro += valor
    