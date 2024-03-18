from constant import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi")

POS_X = 132
POS_Y = 12
SIDE = 72

def initialize():
    res = [0] * 64
    res[27] = res[36] = 1
    res[28] = res[35] = -1
    return res, 1

# le plateau
p, tour = initialize()

def score(p):
    return sum(p)

def laser(pos, d):
    p = pos + d
    if 0 <= p < 64 and abs((pos % 8) - (p % 8)) <= 1:
        return [p] + laser(p, d)
    return []

def jouer(p, tour, coup):
    if p[coup] != 0:
        return p, tour

    q = p[:]
    q[coup] = tour

    nb = False # des pions ont été retournés
    for d in [-9, -8, -7, -1, 1, 7, 8, 9]:
        l = laser(coup, d)
        if len(l) > 0 and q[l[0]] == -tour:
            i = 1
            while i < len(l) and q[l[i]] == -tour:
                i = i + 1
            if i < len(l) and q[l[i]] == tour:
                nb = True
                for ll in range(i):
                    q[l[ll]] = tour

    if not nb:
        print('Coup impossible')
        return p, tour

    return q, -tour

running = True
while running:

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = (event.pos[0] - POS_X) // SIDE
                y = (event.pos[1] - POS_Y) // SIDE
                if 0 <= x < 8 and 0 <= y < 8:
                    print (f'Click on {x}-{y}')
                    p, tour = jouer(p, tour, x + 8 * y)

        # Affichage
        SCREEN.fill(BLACK)
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(SCREEN, GREEN, (x*SIDE+POS_X, y*SIDE+POS_Y, 70, 70))
                v = p[x + y * 8]
                if v == 1:
                    pygame.draw.circle(SCREEN, WHITE,
                        (int((x+0.5)*SIDE+POS_X), int((y+0.5)*SIDE+POS_Y)), 34)
                elif v == -1:
                    pygame.draw.circle(SCREEN, BLACK,
                        (int((x+0.5)*SIDE+POS_X), int((y+0.5)*SIDE+POS_Y)), 34)

        # Affichage du score
        score_text = font.render(f"Score: {score(p)}", True, RED)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)


pygame.quit()
