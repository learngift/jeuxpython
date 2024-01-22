from constant import *
import csv
import math


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editeur de trajectoire d'UFO")

def save_points():
    with open('traj_ufo.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        pos = None

        for point in points:
            if pos == None:
                pos = point
                writer.writerow(pos)
            else:
                nb_points = int(math.sqrt((point[1]-pos[1]) ** 2 + (point[0]-pos[0]) ** 2) / 5)
                for _ in range(nb_points):
                    angle = math.atan2(point[1]-pos[1], point[0]-pos[0])
                    dx = int(5 * math.cos(angle))
                    dy = int(5 * math.cos(angle))
                    pos = pos[0] + dx, pos[1] + dx
                    writer.writerow(pos)
                
    print('Points ecrits dans traj_ufo.csv')



points = []

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

    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    if len(points) > 1:
        pygame.draw.lines(SCREEN, (255, 255, 0), False, points)
    elif len(points) == 1:
        pygame.draw.rect(SCREEN, (255, 255, 0), pygame.Rect(points[0][0], points[0][1], 2, 2))


    pygame.display.flip()

pygame.quit()
