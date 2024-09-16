
# https://fr.wikipedia.org/wiki/Jeu_de_la_vie

import pygame
import random

WIDTH, HEIGHT = 800, 600

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la vie")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

N = 1024
T = [0] * N * N
Z = 15

def evolve():
    global T
    V = list(T)
    for i in range (N + 1, N * (N - 1) - 1):
        nb = T[i - N - 1] + T[i - N] + T[i - N + 1] \
            + T[i - 1] + T[i + 1] \
            + T[i + N - 1] + T[i + N] + T[i + N + 1]
        if nb == 2:
            pass
        elif nb == 3:
            V[i] = 1
        else:
            V[i] = 0
    T = V

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0] - 100
            y = event.pos[1]
            if 0 <= x < HEIGHT and 0 <= y < HEIGHT:
                i = (x//Z) + (y//Z) * N
                T[i] = 1 - T[i]

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                evolve()

    SCREEN.fill((255, 255, 255))
    count_max = HEIGHT // Z
    for x in range(0, count_max):
        for y in range(0, count_max):
            i = x + y * N
            if T[i] != 0:
                pygame.draw.rect(SCREEN, (0, 0, 0), \
                    pygame.Rect(100 + x * Z, y * Z, Z, Z))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()