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

    def desenhar(self, tela):
        # definir animação do pássaro
        self.contagem_imagem += 1
        # a cada tempo de animação a imagem muda
        if self.contagem_imagem < self.TEMPO_DE_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_DE_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_DE_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_DE_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o pássaro estiver caindo não bate a asa
        if self.angulo <= 80:
            self.imagem = self.IMGS[1]
            # e a proxima batida de asa vai ser pra baixo
            self.contagem_imagem = self.TEMPO_DE_ANIMACAO*2

        # desenhar a imagem
        rotacionando_imagem = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = rotacionando_imagem.get_rect(center=pos_centro_imagem)
        tela.blit(rotacionando_imagem, retangulo.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.imagem)

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5