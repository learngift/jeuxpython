from constant import *
from hostile_shoot import Hostile_Shoot
from spaceship import Spaceship

# Chargez l'image du spaceship
spaceship_img = pygame.image.load("spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (64, 32))

shoot2_sound = pygame.mixer.Sound('NovaShot.ogg')

# Liste des tirs
hostile_shoots = pygame.sprite.Group()

class Ufo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, WIDTH - 64), 0, 64, 32)
        self.image = spaceship_img

    def update(self):
        if random.randint(0, 100) < 2:
            global hostile_shoots
            hostile_shoots.add(Hostile_Shoot(self.rect, Spaceship.INSTANCE.rect))
            pygame.mixer.Sound.play(shoot2_sound)

        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)
        self.rect.x = max(0, min(self.rect.x, WIDTH - 64))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - 32))
