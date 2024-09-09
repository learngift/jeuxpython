from constant import *
import random, math

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animations comme tixy.land")

clock = pygame.time.Clock()

t = 0

def compute_diameter(t, i, x, y):
    # Exemple d'une fonction trigonométrique qui varie en fonction de t, i, x et y
    # return math.sin(0.1 * x + 0.1 * y + t)
    # return random.random() < 0.1
    # return random.random()
    return math.sin(t)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.KEYDOWN:
            pass

    SCREEN.fill(BLACK)
    i = 0
    for y in range(16):
        for x in range(16):
            d = compute_diameter(t/50, i, x, y)
            if d > 1.0:
                d = 1.0
            if d < -1.0:
                d = -1.0
            color = WHITE
            if d < 0.0:
                color = (255, 34, 68)
                d = -d
            pygame.draw.circle(SCREEN, color, \
                    (175+x*30, 75+y*30), int(d*15))

    pygame.display.flip()
    clock.tick(30)
    t = t + 1

pygame.quit()
