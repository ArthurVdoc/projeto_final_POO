from abc import ABC, abstractmethod

class Manu(ABC):
    @abstractmethod
    def desenhar(self, tela):
        pass

    @abstractmethod
    def tratar_evento(self, evento):
        pass
