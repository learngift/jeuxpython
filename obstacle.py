from constant import *

OBSTACLES_SPEED = 5

asteroid_img = pygame.image.load("star2.png")
asteroid_img = pygame.transform.scale(asteroid_img, (32, 32))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, WIDTH - 32), 0, 32, 32)
        self.image = asteroid_img

    def update(self):
        self.rect.y += OBSTACLES_SPEED
        if self.rect.y > HEIGHT:
            self.kill()