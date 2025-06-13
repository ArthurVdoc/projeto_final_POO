from abc import ABC, abstractmethod

class Morador(ABC):
    @abstractmethod
    def custo(self) -> int:
        pass
    @abstractmethod
    def rendimento_dia(self) -> int:
        pass