from constant import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi")

POS_X = 132
POS_Y = 12
SIDE = 72
DIRECTIONS = [-9, -8, -7, -1, 1, 7, 8, 9]


def initialize():
    #return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, -1, 0, 0, 1, -1, -1, -1, -1, -1, 0, 0, 1, -1, -1, -1, -1, -1, 0, 0, 1, 1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], -1
    res = [0] * 64
    res[27] = res[36] = 1
    res[28] = res[35] = -1
    return res, 1

# le plateau
p, tour = initialize()

fit = [ 10, -5, 1, 1, 1, 1, -5, 10,
        -5, -5, 1, 1, 1, 1, -5, -5,
        1, 1, 3, 1, 1, 3, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 3, 1, 1, 3, 1, 1,
        -5, -5, 1, 1, 1, 1, -5, -5,
        10, -5, 1, 1, 1, 1, -5, 10 ]

def score_fit(p):
    res = 0
    for i in range(len(p)):
        res = res + p[i] * fit[i]
    return res

def score(p):
    return sum(p)

def print_plateau(p):
    a = ['X', ' ', 'O']
    print('+--------+')
    for y in range(8):
        print('|' + ''.join([a[1+p[y*8+x]] for x in range(8)]) + '|')
    print('+--------+')

# renvoie le nombre de pions retournés dans une direction
def laser(pos, d, plateau, tour):
    res = 0 # compte le nombre de pions adverses avant de rencontrer notre pion
    np = pos + d # position suivante
    while 0 <= np < 64 and -1 <= (pos % 8) - (np % 8) <= 1:
        c = plateau[np] # couleur dans la case np
        if c == 0: # case vide
            return 0
        elif c == tour:
            return res
        pos, np = np, np + d
        res += 1
    return 0

def coup_possible(pos, plateau, tour):
    return any(laser(pos, d, plateau, tour) > 0 for d in DIRECTIONS)

def coups_possible(plateau, tour):
    return [ pos for pos in range(64) if (plateau[pos] == 0) & coup_possible(pos, plateau, tour) ]

def minmax(plateau, tour, depth, alpha, beta):
    current_score = score_fit(plateau) * tour
    if depth == 0:
        return current_score
    coups = coups_possible(plateau, tour)
    if len(coups) == 0:
        # il faut passer son tour
        return -minmax(plateau, -tour, depth - 1, -beta, -alpha)

    valeur_max = float('-inf')
    for coup in coups:
        plateau2, tour2 = jouer(plateau, tour, coup)
        score_coup = -minmax(plateau2, -tour, depth - 1, -beta, -alpha)
        if score_coup > valeur_max:
            valeur_max = score_coup
            alpha = max(alpha, valeur_max)
            if alpha >= beta:
                break
    return valeur_max

def choisir_coup():
    global p, tour
    coups = coups_possible(p, tour)
    if len(coups) == 0:
        print("Pas de coup possible: la partie est probablement déjà finie")
        return
    meilleur_coup = None
    meilleur_score = -65000
    alpha, beta = float('-inf'), float('inf')
    for coup in coups:
        plateau2, tour2 = jouer(p, tour, coup)
        nouveau_score = -minmax(plateau2, -tour, 4, -beta, -alpha)
        if nouveau_score > meilleur_score:
            meilleur_score = nouveau_score
            meilleur_coup = coup
            alpha = meilleur_score
    if meilleur_coup is not None:
        p, tour = jouer(p, tour, meilleur_coup)
        print (f'ordi play on {1+meilleur_coup%8}-{1+meilleur_coup//8}')

def jouer(p, tour, coup):
    if p[coup] != 0:
        return p, tour

    q = p[:]
    q[coup] = tour

    nb = False # des pions ont été retournés
    for d in DIRECTIONS:
        l = laser(coup, d, p, tour)
        if l > 0:
            nb = True
            for i in range(1, l + 1):
                q[coup + d * i] = tour

    if not nb:
        print('Coup impossible')
        return p, tour
    if len(coups_possible(q, -tour)) == 0:
        if len(coups_possible(q, tour)) == 0:
            print (f'Game Over: score {score(q)}')
            return q, tour
        else:
            print ('No move: pass')
            return q, tour
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    print("demande à l'ordi de jouer")
                    choisir_coup()
                elif event.key == pygame.K_r:
                    p, tour = initialize()


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
                elif coup_possible(x + y * 8, p, tour):
                    pygame.draw.circle(SCREEN, BLACK,
                        (int((x+0.5)*SIDE+POS_X), int((y+0.5)*SIDE+POS_Y)), 2)


        # Affichage du score
        score_text = font.render(f"Score: {score(p)}", True, RED)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)


pygame.quit()
