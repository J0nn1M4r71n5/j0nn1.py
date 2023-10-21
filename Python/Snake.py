
import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
cor_branca = (255, 255, 255)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)

# Configurações do jogo
largura, altura = 800, 600
tamanho_cobra = 20
velocidade = 15

# Inicialização da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Função para desenhar a cobra na tela
def desenhar_cobra(cobra, tamanho_cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, cor_verde, [segmento[0], segmento[1], tamanho_cobra, tamanho_cobra])

# Função principal do jogo
def jogo():
    jogo_ativo = True

    # Posição inicial da cobra
    x_cobra, y_cobra = largura / 2, altura / 2
    x_cobra_mudanca, y_cobra_mudanca = 0, 0

    # Lista para armazenar os segmentos da cobra
    cobra = []
    comprimento_cobra = 1

    # Posição inicial da maçã
    x_maca = round(random.randrange(0, largura - tamanho_cobra) / 20.0) * 20.0
    y_maca = round(random.randrange(0, altura - tamanho_cobra) / 20.0) * 20.0

    while jogo_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -tamanho_cobra
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = tamanho_cobra
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -tamanho_cobra
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = tamanho_cobra
                    x_cobra_mudanca = 0

        # Atualiza a posição da cobra
        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca

        # Verifica se a cobra atingiu a borda da tela
        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            jogo_ativo = False

        tela.fill(cor_branca)
        pygame.draw.rect(tela, cor_vermelha, [x_maca, y_maca, tamanho_cobra, tamanho_cobra])
        cobra_cabeca = []
        cobra_cabeca.append(x_cobra)
        cobra_cabeca.append(y_cobra)
        cobra.append(cobra_cabeca)

        # Mantém o comprimento da cobra
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verifica se a cobra comeu a maçã
        if x_cobra == x_maca and y_cobra == y_maca:
            x_maca = round(random.randrange(0, largura - tamanho_cobra) / 20.0) * 20.0
            y_maca = round(random.randrange(0, altura - tamanho_cobra) / 20.0) * 20.0
            comprimento_cobra += 1

        # Verifica se a cobra colidiu consigo mesma
        for segmento in cobra[:-1]:
            if segmento == cobra_cabeca:
                jogo_ativo = False

        # Desenha a cobra na tela
        desenhar_cobra(cobra, tamanho_cobra)

        # Atualiza a tela
        pygame.display.update()

        # Controle de velocidade
        time.sleep(velocidade / 10.0)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
