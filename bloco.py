import pygame
import constantes

class Bloco:
    def __init__(self, cord_x, cord_y, tamanho):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.tamanho = tamanho
        self.tem_construção = False

    def desenhar(self, tela):
        if self.tem_construção:
            cor = constantes.MARROM
        else:
            cor = constantes.VERDE

