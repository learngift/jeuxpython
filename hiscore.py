import csv
from constant import *


def read_hiscores():
    """ Read hi-score file """
    hiscores = []
    try:
        with open('hiscores.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                hiscore = (int(row[0]), row[1])
                hiscores.append(hiscore)
    except FileNotFoundError:
        hiscores = [ (i, '------') for i in range(20) ]
    hiscores.sort()
    return hiscores

def save_hiscores():
    with open('hiscores.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for hiscore in hiscores:
            writer.writerow(hiscore)


hiscores = read_hiscores()

def add_score(score):
    if score < hiscores[0][0]:
        print(f'Vous n\'avez pas un hiscore, il fallait battre {hiscores[0][0]}')
        return
    name = input('Vous avez un hiscore, quel est votre nom ?')
    hiscores.pop(0)
    i = 0
    while (i < len(hiscores) and score > hiscores[i][0]):
        i = i + 1
    hiscores.insert(i, (score, name))
    save_hiscores()

def display_hall_of_fame():
    '''renvoit False pour arréter de jouer'''
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jeu de Tir Spatial")

    play_rect = pygame.Rect(150, 550, 100, 30)
    quit_rect = pygame.Rect(550, 550, 100, 30)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    return False
                print(f'Click({event.pos})')

        SCREEN.fill(BLACK)

        # Affichage des boutons
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(SCREEN, RED, pygame.Rect(50, 50, 10, 10))
        pygame.draw.rect(SCREEN, BLUE, play_rect)
        SCREEN.blit(font.render("Play", True, RED), (155, 555))
        SCREEN.blit(font.render("Quit", True, BLUE), (555, 555))

        pygame.display.flip()
        clock.tick(30)

#display_hall_of_fame()
#pygame.quit()