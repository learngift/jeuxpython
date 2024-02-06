from constant import *
from obstacle import Obstacle
from spaceship import Spaceship, bullets
from hostile_shoot import Hostile_Shoot, hostile_shoots
from ufo1 import Ufo1
from ufo2 import Ufo2
from bonus import Bonus

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir Spatial")

# Groupes pour les astéroïdes et les ovnis
obstacles2 = pygame.sprite.Group()
obstacles3 = pygame.sprite.Group() # ovnis

# Groupe pour notre vaisseau spacial
spaceship = pygame.sprite.Group()
spaceship.add(Spaceship())
autre = pygame.sprite.Group()

all_groups = [obstacles2, obstacles3, spaceship, bullets, hostile_shoots, autre]
# Score
score = 0

clock = pygame.time.Clock()

wave = 1
nb_ufo1_killed = 0
nb_ufo2 = 0 # number of ufo2 created

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Génération d'obstacles
    if random.randint(0, 100) < 5:
        obstacles2.add(Obstacle())
    if wave == 1:
        if (len(obstacles3) < 2) and (random.randint(0, 100) < 1):
            obstacles3.add(Ufo1())
    elif wave == 2:
        if nb_ufo2 < 9 and Ufo2.i > 30 * nb_ufo2:
            obstacles3.add(Ufo2(nb_ufo2))
            nb_ufo2 = nb_ufo2 + 1
        Ufo2.i = Ufo2.i + 1

    # Génération du bonus
    if random.randint(0, 1000) < 2:
        autre.add(Bonus())


    # Détection de collision
    if pygame.sprite.groupcollide(spaceship, obstacles2, True, True):
        running = False
    if pygame.sprite.groupcollide(spaceship, hostile_shoots, True, True):
        running = False

    if pygame.sprite.groupcollide(bullets, autre, True, True):
        Spaceship.INSTANCE.bonus()
    # Détection de collision des tirs avec les astéroïdes
    if pygame.sprite.groupcollide(bullets, obstacles3, True, True):
        score += 50
        if wave == 1:
            nb_ufo1_killed = nb_ufo1_killed + 1
            if nb_ufo1_killed == 10:
                wave = 2
                Ufo2.i = 0
        elif wave == 2:
            if len(obstacles3) == 0:
                wave = 1
                nb_ufo1_killed = 0

    if pygame.sprite.groupcollide(bullets, obstacles2, True, True):
        score += 10

    # Affichage
    SCREEN.fill(WHITE)

    # Affichage de la route
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    for g in all_groups:
        g.update()
        g.draw(SCREEN)

    # Affichage du score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, RED)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

# Affichage du score final dans la console
print(f"Score final : {score}")