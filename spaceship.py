from constant import *

# Chargez l'image du vaisseau spatial du joueur
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (64, 64))

shoot_sound = pygame.mixer.Sound('Normal shot.ogg')

# liste des tirs
bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Déplacement des tirs du joueur
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

class Spaceship(pygame.sprite.Sprite):
    INSTANCE = None
    def __init__(self):
        super().__init__()
        self.rect = player_img.get_rect()
        self.rect.x =  WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT - self.rect.height - 20
        self.image = player_img
        Spaceship.INSTANCE = self

    def update(self):
        # Déplacement du vaisseau spatial du joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        # Tir du joueur
        global bullets
        if keys[pygame.K_SPACE]:
            bullets.add(Bullet(self.rect.centerx - 2, self.rect.top - 10))
            pygame.mixer.Sound.play(shoot_sound)

        # Limitez le vaisseau spatial aux limites de l'écran
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
