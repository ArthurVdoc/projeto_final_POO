import pygame
import constantes

class CarregarSprites:
    _sprites = {}

    @classmethod
    def carregar_sprites(cls):
        if cls._sprites:
            return cls._sprites
        
        cls._sprites = {
            constantes.VAZIO: pygame.image.load("imagens/grama.png").convert_alpha(),
            constantes.CASA: pygame.image.load("imagens/casa.png").convert_alpha(),
            constantes.TAVERNA: pygame.image.load("imagens/taverna.png").convert_alpha(),
            constantes.FAZENDEIRO: pygame.image.load("imagens/fazendeiro.png").convert_alpha(),
            constantes.CAÇADOR: pygame.image.load("imagens/caçador.png").convert_alpha(),
            constantes.CAMINHO: pygame.image.load("imagens/caminho.png").convert_alpha(),
        }

        return cls._sprites
    
    @classmethod
    def get_sprite(cls,estado):
        return cls._sprites.get(estado, None)