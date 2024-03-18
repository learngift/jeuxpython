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

def add_score(score, SCREEN):
    # Affichage du score final dans la console
    print(f"Score final : {score}")
    if score < hiscores[0][0]:
        print(f'Vous n\'avez pas un hiscore, il fallait battre {hiscores[0][0]}')
        return display_hall_of_fame(SCREEN)

    name = ask_your_name(score, SCREEN)
    # name = input('Vous avez un hiscore, quel est votre nom ?')

    hiscores.pop(0)
    i = 0
    while (i < len(hiscores) and score > hiscores[i][0]):
        i = i + 1
    hiscores.insert(i, (score, name))
    save_hiscores()
    return display_hall_of_fame(SCREEN)

def ask_your_name(score, SCREEN):
    name = ''
    name_rect = pygame.Rect(200, 350, 400, 60)
    ok_rect  = pygame.Rect(380, 530, 40, 30)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if ok_rect.collidepoint(event.pos):
                    return name
            elif event.type == pygame.KEYDOWN:
                if pygame.K_SPACE <= event.key <= pygame.K_z:
                    k = event.key
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        k = k - 32
                    k = chr(k)
                    if k == 'a' :
                        k = 'q'
                    elif k == 'q':
                        k = 'a'
                    elif k == 'A':
                        k = 'Q'
                    elif k == 'Q':
                        k = 'A'
                    elif k == 'z':
                        k = 'w'
                    elif k == 'w':
                        k = 'z'
                    elif k == 'Z':
                        k = 'W'
                    elif k == 'W':
                        k = 'Z'
                    name = name + k
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
        SCREEN.fill(BLACK)

        # Affichage des boutons
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(SCREEN, BLUE, name_rect, 4)
        SCREEN.blit(font.render(name, True, YELLOW), (310, 355))
        SCREEN.blit(font.render("OK", True, BLUE), (382, 535))

        SCREEN.blit(font.render("Bravo ! Vous avez un hiscore,", True, YELLOW), (220, 70))
        SCREEN.blit(font.render("quel est votre nom ?", True, YELLOW), (270, 150))

        pygame.display.flip()
        clock.tick(30)

def display_hall_of_fame(SCREEN):
    '''renvoit False pour arréter de jouer'''
    pygame.display.set_caption("Jeu de Tir Spatial")

    play_rect = pygame.Rect(150, 550, 80, 30)
    quit_rect = pygame.Rect(550, 550, 80, 30)
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

        pygame.draw.rect(SCREEN, BLUE, play_rect)
        SCREEN.blit(font.render("Play", True, RED), (155, 555))
        SCREEN.blit(font.render("Quit", True, BLUE), (555, 555))

        SCREEN.blit(font.render("Hall of Fame", True, YELLOW), (360, 10))
        for i in range(len(hiscores)):
            x = 10 if i < 10 else 10 + WIDTH / 2
            hiscore = hiscores[len(hiscores) - i -1]
            SCREEN.blit(font.render(hiscore[1], True, WHITE),
                                    (x, 120 + 36 * (i % 10)))
            x = 310 if i < 10 else 310 + WIDTH / 2
            SCREEN.blit(font.render(str(hiscore[0]), True, WHITE),
                                    (x, 120 + 36 * (i % 10)))

        pygame.display.flip()
        clock.tick(30)

# ask_your_name(100, pygame.display.set_mode((WIDTH, HEIGHT)))
# display_hall_of_fame(pygame.display.set_mode((WIDTH, HEIGHT)))
# pygame.quit()


