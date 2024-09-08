from constant import *
import random

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animations")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
dx1, dy1 = 4, 3  # Vitesse de l'extrémité 1
dx2, dy2 = 5, 2  # Vitesse de l'extrémité 2

# Couleur initiale
color = (255, 255, 255)
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.KEYDOWN:
            pass

    trail_surface.fill((0, 0, 0, 15), special_flags=pygame.BLEND_RGBA_SUB)

    # Calculer les nouvelles positions pour les deux extrémités de la ligne
    x1 += dx1
    y1 += dy1
    x2 += dx2
    y2 += dy2

    # Vérifier les collisions pour l'extrémité 1
    if x1 <= 0 or x1 >= WIDTH:
        dx1 = -dx1
        color = random_color()  # Changer la couleur en cas de collision
    if y1 <= 0 or y1 >= HEIGHT:
        dy1 = -dy1
        color = random_color()

    # Vérifier les collisions pour l'extrémité 2
    if x2 <= 0 or x2 >= WIDTH:
        dx2 = -dx2
        color = random_color()
    if y2 <= 0 or y2 >= HEIGHT:
        dy2 = -dy2
        color = random_color()

    # Dessiner la ligne sur la surface de traînée
    pygame.draw.line(trail_surface, color, (x1, y1), (x2, y2), 5)

    # Dessiner la surface de traînée avec l'effet de fondu sur l'écran
    SCREEN.blit(trail_surface, (0, 0))
    # Affichage du score
    # score_text = font.render(f"Score: {score(p)}", True, RED)
    # SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)


pygame.quit()
