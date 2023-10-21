import random
import pygame

# Inicialização do Pygame
pygame.init()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configurações do jogo
LARGURA, ALTURA = 400, 500
TAMANHO_BLOCO = 20
VELOCIDADE_QUEDA = 1

# Inicialização da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris")

# Formas possíveis
formas = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]

# Função para criar uma nova peça
def nova_peca():
    forma = random.choice(formas)
    cor = random.choice([AZUL, VERMELHO, VERDE])
    x = (LARGURA - len(forma[0]) * TAMANHO_BLOCO) // 2
    y = 0
    return forma, cor, x, y

# Função para desenhar uma peça na tela
def desenhar_peca(peca, cor, x, y):
    for i in range(len(peca)):
        for j in range(len(peca)[i]):
            if peca[i][j]:
                pygame.draw.rect(tela, cor, (x + j * TAMANHO_BLOCO, y + i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

# Função principal do jogo
def jogo():
    jogo_ativo = True
    peca, cor, x, y = nova_peca()

    relogio = pygame.time.Clock()

    while jogo_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x -= TAMANHO_BLOCO
                if evento.key == pygame.K_RIGHT:
                    x += TAMANHO_BLOCO
                if evento.key == pygame.K_DOWN:
                    y += TAMANHO_BLOCO

        # Movimentação automática da peça para baixo
        y += VELOCIDADE_QUEDA

        # Colisão com a parte inferior ou outras peças
        if colisao(peca, x, y):
            y -= VELOCIDADE_QUEDA
            if y == 0:
                jogo_ativo = False
            else:
                peca, cor, x, y = nova_peca()

        # Limpar a tela
        tela.fill(PRETO)

        # Desenhar a peça atual
        desenhar_peca(peca, cor, x, y)

        pygame.display.update()
        relogio.tick(60)

    pygame.quit()
    quit()

# Função para verificar colisões
def colisao(peca, x, y):
    for i in range(len(peca)):
        for j in range(len(peca)[i]):
            if peca[i][j]:
                if x + j * TAMANHO_BLOCO < 0 or x + j * TAMANHO_BLOCO >= LARGURA or y + i * TAMANHO_BLOCO >= ALTURA:
                    return True
    return False

# Iniciar o jogo
jogo()
