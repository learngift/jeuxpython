from constant import *

BONUS_SPEED = 5

bonus_img = pygame.image.load("diamond2.png")
bonus_img = pygame.transform.scale(bonus_img, (32, 32))


class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, WIDTH - 32), 0, 32, 32)
        self.image = bonus_img

    def update(self):
        self.rect.y += BONUS_SPEED
        if self.rect.y > HEIGHT:
            self.kill()