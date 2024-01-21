from constant import *

# Liste des tirs
hostile_shoots = pygame.sprite.Group()

class Hostile_Shoot(pygame.sprite.Sprite):
    def __init__(self, ship, player):
        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.x = ship.x + 32
        self.rect.y = ship.y + 32
        self.angle = math.atan2(player.y-self.rect.y, player.x-self.rect.x)

    def update(self):
        self.rect.x += 5 * math.cos(self.angle)
        self.rect.y += 5 * math.sin(self.angle)
        if not self.on_screen():
            self.kill()

    def on_screen(self):
        return (0 < self.rect.x < WIDTH) and (0 < self.rect.y < HEIGHT)