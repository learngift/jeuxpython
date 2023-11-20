from constant import *
from obstacle import Obstacle
from spaceship import Spaceship, bullets
from hostile_shoot import Hostile_Shoot
from ufo1 import Ufo1, hostile_shoots

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir Spatial")

# Groupe pour les astéroïdes et les ovnis
obstacles2 = pygame.sprite.Group()

# Groupe pour notre vaisseau spacial
spaceship = pygame.sprite.Group()
spaceship.add(Spaceship())

ships = []

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
    if (len(ships) < 2) and (random.randint(0, 100) < 1):
        obstacle = Ufo1()
        ships.append(obstacle)
        obstacles2.add(obstacle)

    player_rect = Spaceship.INSTANCE.rect

    # Détection de collision
    for obstacle2 in obstacles2:
        if player_rect.colliderect(obstacle2):
            running = False

    for s in hostile_shoots:
        if player_rect.collidepoint(s.x, s.y):
            running = False

    # Détection de collision des tirs avec les astéroïdes
    for bullet in bullets:
        for obstacle2 in obstacles2:
            if bullet.colliderect(obstacle2.rect):
                try:
                    bullets.remove(bullet)
                    obstacle2.kill()
                except ValueError:
                    pass
                score += 10
        for ship in ships:
            if bullet.colliderect(ship):
                ships.remove(ship)
                ship.kill()
                try:
                    bullets.remove(bullet)
                except ValueError:
                    pass
                score += 50

    # Affichage
    SCREEN.fill(WHITE)

    # Affichage de la route
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    # Affichage du vaisseau spatial du joueur
    # SCREEN.blit(player_img, player_rect)
    spaceship.update()
    spaceship.draw(SCREEN)

    obstacles2.update()
    obstacles2.draw(SCREEN)

    # Affichage des tirs
    for bullet in bullets:
        pygame.draw.rect(SCREEN, RED, bullet)
    for s in hostile_shoots:
        pygame.draw.line(SCREEN, (0, 255, 0), (s.x, s.y), (s.x, s.y))
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