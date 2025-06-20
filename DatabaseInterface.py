from abc import ABC,abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def criar():
        pass

    @abstractmethod
    def carregar():
        pass

    @abstractmethod
    def extrair():
        pass
    
    @abstractmethod
    def alterar():
        pass

    @abstractmethod
    def deletar():
        pass