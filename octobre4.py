from constant import *
from obstacle import Obstacle
from spaceship import Spaceship, bullets
from hostile_shoot import Hostile_Shoot
from ufo1 import Ufo1, hostile_shoots

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir Spatial")

# Groupes pour les astéroïdes et les ovnis
obstacles2 = pygame.sprite.Group()
obstacles3 = pygame.sprite.Group() # ovnis

# Groupe pour notre vaisseau spacial
spaceship = pygame.sprite.Group()
spaceship.add(Spaceship())

# Score
score = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Génération d'obstacles
    if random.randint(0, 100) < 5:
        obstacles2.add(Obstacle())
    if (len(obstacles3) < 2) and (random.randint(0, 100) < 1):
        obstacles3.add(Ufo1())

    player_rect = Spaceship.INSTANCE.rect

    # Détection de collision
    if pygame.sprite.groupcollide(spaceship, obstacles2, True, True):
        running = False

    for s in hostile_shoots:
        if player_rect.collidepoint(s.rect.x, s.rect.y):
            running = False

    # Détection de collision des tirs avec les astéroïdes
    if pygame.sprite.groupcollide(bullets, obstacles3, True, True):
        score += 50

    if pygame.sprite.groupcollide(bullets, obstacles2, True, True):
        score += 10

    # Affichage
    SCREEN.fill(WHITE)

    # Affichage de la route
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    # Affichage du vaisseau spatial du joueur
    spaceship.update()
    spaceship.draw(SCREEN)

    obstacles2.update()
    obstacles2.draw(SCREEN)
    obstacles3.update()
    obstacles3.draw(SCREEN)

    # Affichage des tirs
    bullets.update()
    bullets.draw(SCREEN)

    for s in hostile_shoots:
        pygame.draw.line(SCREEN, (0, 255, 0), (s.rect.x, s.rect.y), (s.rect.x, s.rect.y))
        s.update()

    # Affichage du score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, RED)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

# Affichage du score final dans la console
print(f"Score final : {score}")