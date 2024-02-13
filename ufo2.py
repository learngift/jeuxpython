from constant import *
from hostile_shoot import Hostile_Shoot, hostile_shoots
from spaceship import Spaceship
import csv

# Chargez l'image du spaceship
spaceship_img = pygame.image.load("images/ufo2_3.png")
spaceship_img = pygame.transform.scale(spaceship_img, (32, 32))
spaceship2_img = pygame.image.load("images/ufo2_4.png")
spaceship2_img = pygame.transform.scale(spaceship2_img, (32, 32))

shoot2_sound = pygame.mixer.Sound('NovaShot.ogg')

def lire_points(filename):
    """ Lit des points à partir d'un fichier CSV et les retourne sous forme de liste de tuples. """
    points = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            point = (int(row[0]), int(row[1]))
            points.append(point)
    return points

points = lire_points('traj_ufo1.csv')

class Ufo2(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, WIDTH - 64), 0, 64, 32)
        self.image = spaceship_img
        self.count = 0
        self.id = id

    def update(self):
        if self.count == 0:
            self.image = spaceship_img
        elif self.count == 30:
            self.image = spaceship2_img

        if self.count == 60:
            self.count = 0
        else:
            self.count = self.count + 1

        if random.randint(0, 100) < 2 and self.rect.y < 200:
            global hostile_shoots
            hostile_shoots.add(Hostile_Shoot(self.rect, Spaceship.INSTANCE.rect))
            pygame.mixer.Sound.play(shoot2_sound)

        k = (Ufo2.i - 30 * self.id)  % len(points)
        self.rect.x = points[k][0]
        self.rect.y = points[k][1]

        if Ufo2.i > 2 * len(points):
            Ufo2.i = len(points)
