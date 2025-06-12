from utilidades.carregar_sprites import CarregarSprites
import pygame
import constantes

class Bloco:
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.tamanho = constantes.TAMANHO_BLOCO
        self.estado = constantes.VAZIO
        self.sprites = CarregarSprites.carregar_sprites()

    def desenhar(self, tela):
        if self.estado == constantes.CASA:
            cor = constantes.MARROM
        elif self.estado == constantes.TAVERNA:
            cor = constantes.CINZA
        elif self.estado == constantes.FAZENDEIRO:
            cor = constantes.AMARELO
        elif self.estado == constantes.CAÇADOR:
            cor = constantes.ROXO
        elif self.estado == constantes.CAMINHO:
            cor = constantes.CINZA
        else:
            cor = constantes.VERDE

        pixel_x = self.cord_x*self.tamanho
        pixel_y = self.cord_y*self.tamanho

        retangulo = pygame.Rect(pixel_x, pixel_y, self.tamanho, self.tamanho)      
        pygame.draw.rect(tela, cor, retangulo)
        #pygame.draw.rect(tela, constantes.PRETO, retangulo, 1)

        sprite = self.sprites.get(self.estado)
        grama = self.sprites.get(constantes.VAZIO)
        if sprite:
            grama_redimensionada =  pygame.transform.scale(grama, 
                                                           (self.tamanho, 
                                                            self.tamanho))
            tela.blit(grama_redimensionada, (pixel_x, pixel_y))
            sprite_redimensionado = pygame.transform.scale(sprite, 
                                                           (self.tamanho, 
                                                            self.tamanho))
            tela.blit(sprite_redimensionado, (pixel_x, pixel_y))
    
    def definir_estado(self, novo_estado):
        self.estado = novo_estado




