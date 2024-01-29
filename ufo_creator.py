from constant import *
import csv
import math


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editeur de trajectoire d'UFO")

def interpolate(pts):
    res = [pts[0]]
    pos = None

    speed = 5

    for point in pts:
        if pos == None:
            pos = point
        else:
            nb_points = int(math.sqrt((point[1]-pos[1]) ** 2 + (point[0]-pos[0]) ** 2) / speed)
            for _ in range(nb_points):
                angle = math.atan2(point[1]-pos[1], point[0]-pos[0])
                dx = int(speed * math.cos(angle))
                dy = int(speed * math.sin(angle))
                pos = pos[0] + dx, pos[1] + dy
                res.append(pos)
    return res

def save_points():
    with open('traj_ufo.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for point in interpolate(points):
            writer.writerow(point)

    print('Points ecrits dans traj_ufo.csv')


points = []
clock = pygame.time.Clock()

def test():
    spaceship_img = pygame.image.load("images/ufo2_4.png")
    spaceship_img = pygame.transform.scale(spaceship_img, (32, 32))
    spaceship_rect = spaceship_img.get_rect()
    i = 0
    pts = interpolate(points)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return
        spaceship_rect.x = pts[i][0]
        spaceship_rect.y = pts[i][1]

        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
        pygame.draw.lines(SCREEN, (255, 255, 0), False, points)

        SCREEN.blit(spaceship_img, spaceship_rect)

        pygame.display.flip()
        clock.tick(30)

        i = i + 1
        if i == len(pts):
            i = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(points) > 0:
                points.pop()
            if event.key == pygame.K_s:
                save_points()
            if event.key == pygame.K_t:
                test()

    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    if len(points) > 1:
        pygame.draw.lines(SCREEN, (255, 255, 0), False, points)
    elif len(points) == 1:
        pygame.draw.rect(SCREEN, (255, 255, 0), pygame.Rect(points[0][0], points[0][1], 2, 2))


    pygame.display.flip()

pygame.quit()
