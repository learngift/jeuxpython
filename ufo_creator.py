from constant import *
import csv
import math


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editeur de trajectoire d'UFO")

def dist(p1, p2):
    res = 0.0
    for i in range(len(p1)):
        res = res + (p1[i]-p2[i]) ** 2
    return math.sqrt(res)

def interpolate(pts):
    pos = pts.pop(0)
    res = [pos]

    speed = 5

    for point in pts:
        while dist(point, pos) > speed:
            angle = math.atan2(point[1]-pos[1], point[0]-pos[0])
            dx = int(speed * math.cos(angle))
            dy = int(speed * math.sin(angle))
            pos = pos[0] + dx, pos[1] + dy
            res.append(pos)
    pts.insert(0, res[0])
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

        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
        # pygame.draw.lines(SCREEN, (255, 255, 0), False, points)

        for j in range(9):
            k = (i - j * 30) % len(pts)
            if i < j * 30 : continue
            spaceship_rect.x = pts[k][0]
            spaceship_rect.y = pts[k][1]
            SCREEN.blit(spaceship_img, spaceship_rect)


        pygame.display.flip()
        clock.tick(30)

        i = i + 1
        if i == 2 * len(pts):
            i = len(pts)

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
            if event.key == pygame.K_t and len(points) > 2:
                test()

    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    if len(points) > 1:
        pygame.draw.lines(SCREEN, (255, 255, 0), False, points)
    elif len(points) == 1:
        pygame.draw.rect(SCREEN, (255, 255, 0), pygame.Rect(points[0][0], points[0][1], 2, 2))


    pygame.display.flip()

pygame.quit()
