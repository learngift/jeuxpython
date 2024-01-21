from constant import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editeur de trajectoire d'UFO")


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

    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    if len(points) > 1:
        pygame.draw.lines(SCREEN, (255, 255, 0), False, points)
    elif len(points) == 1:
        pygame.draw.rect(SCREEN, (255, 255, 0), pygame.Rect(points[0][0], points[0][1], 2, 2))


    pygame.display.flip()

pygame.quit()
