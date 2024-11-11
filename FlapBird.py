import pygame
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMG_BACKGROUND = pygame.transform.scale2x(pygame.image.load('imgs/bg.png'))
IMG_CHAO = pygame.transform.scale2x(pygame.image.load('imgs/base.png'))
IMG_CANO = pygame.transform.scale2x(pygame.image.load('imgs/pipe.png'))
IMGS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load('imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load('imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load('imgs/bird3.png'))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50, bold=True)


class Passaro:
    IMGS = IMGS_PASSARO
    # animações de rotação do pássaro
    ROTACAO_MAXIMA = 25
    VELOCIDADE_DE_ROTACAO = 20
    TEMPO_DE_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        # define qual imagem da lista estamos usando
        self.contagem_imagem = 0
        self.imagem = Passaro.IMGS[0]

    def pular(self):
        self.velocidade = - 10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        aceleracao = 3
        deslocamento = (aceleracao * (self.tempo**2))/2 + (self.velocidade * self.tempo)
        # restringir o deslocamento vertical máximo
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_DE_ROTACAO


class Cano:
    pass


class Chao:
    pass
