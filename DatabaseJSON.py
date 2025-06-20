from DatabaseInterface import DatabaseInterface
import json
import os

class DatabaseJSON(DatabaseInterface):
    def __init__(self, nome: str):
        self.nome = nome

    def criar(self):
        if not os.path.exists(self.nome):
            with open(self.nome, "w") as f:
                json.dump({}, f)
        with open(self.nome, "r") as f:
            return json.load(f)

    def carregar(self, entrada: dict):
        self.criar()
        with open(self.nome, "w") as f:
            json.dump(entrada, f, indent=4)

    def extrair(self):
        with open(self.nome, "r") as f:
            return json.load(f)

    def alterar(self, chave: str, valor):
        dados = self.extrair()
        dados[chave] = valor
        self.carregar(dados)

    def deletar(self, chave: str):
        dados = self.extrair()
        if chave in dados:
            del dados[chave]
            self.carregar(dados)
