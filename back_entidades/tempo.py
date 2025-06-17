import time

class Tempo:
    def __init__(self):
        self.inicio = time.time()
    
    def dias_passados(self):
        segundos_passados = time.time() - self.inicio
        return int(segundos_passados//10)