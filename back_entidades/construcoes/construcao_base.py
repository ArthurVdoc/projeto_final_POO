from abc import ABC, abstractmethod

class Construção(ABC):
    @abstractmethod
    def custo(self) -> int:
        pass