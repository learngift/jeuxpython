from constant import *
import random, math

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animations comme tixy.land")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

t = 0

def f1(t, i, x, y):
    d = y * y % 5.9 + 1
    return 0 if (int(x + t * 50 / d) & 15) else 1/d

fcts = [
    lambda t, i, x, y: math.sin(y/8+t),
    lambda t, i, x, y: random.random() < 0.1,
    lambda t, i, x, y: random.random(),
    lambda t, i, x, y: math.sin(t),
    lambda t, i, x, y: i / 256.0,
    lambda t, i, x, y: x / 16,
    lambda t, i, x, y: y / 16,
    lambda t, i, x, y: y - 7.5,
    lambda t, i, x, y: y - t,
    lambda t, i, x, y: y - t*4,
    lambda t, i, x, y: [1, 0, -1][i%3],
    lambda t, i, x, y: math.sin(t-math.sqrt((x-7.5)**2+(y-6)**2)),
    lambda t, i, x, y: y - x,
    lambda t, i, x, y: 1 if ((y > x) & (14-x < y)) else 0,
    f1,
    lambda t, i, x, y: [5463, 2194, 2386,0,0,0,0,0][int(y + t*9) & 7] & 1 << x,
]
desc = ['math.sin(y/8+t)',
    'random.random() < 0.1',
    'random.random()',
    'math.sin(t)',
    'i / 256',
    'x / 16',
    'y / 16',
    'y - 7.5',
    'y - t',
    'y - t*4',
    '[1, 0, -1][i%3]',
    'math.sin(t-math.sqrt((x-7.5)**2+(y-6)**2))',
    'y: y - x',
    '1 if ((y > x) & (14-x < y)) else 0',
    'd = y * y % 5.9 + 1 ; 0 if (int(x + t * 50 / d) & 15) else 1/d',
    '[5463,2194,2386][y+t*9&7]&1<<x-1'
]

i_fct = 0

def update_text2():
    global text2
    s = ''
    if i_fct < len(desc):
        s = desc[i_fct]
    text2 = font.render(s, 1, WHITE)
update_text2()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                i_fct = i_fct + 1
                if i_fct >= len(fcts):
                    i_fct = 0
            elif event.key == pygame.K_UP:
                i_fct = i_fct - 1
                if i_fct < 0:
                    i_fct = len(fcts) - 1
            update_text2()

    SCREEN.fill(BLACK)
    i = 0
    f = fcts[i_fct]
    for y in range(16):
        for x in range(16):
            d = f(t/50, i, x, y)
            color = WHITE
            if d < 0.0:
                color = (255, 34, 68)
                d = -d
            if d > 1.0:
                d = 1.0
            pygame.draw.circle(SCREEN, color, \
                    (175+x*30, 75+y*30), int(d*15))
            i = i + 1

    text = font.render(f'fps {clock.get_fps():0.2f}', 1, BLUE)
    SCREEN.blit(text, (650, 100))
    SCREEN.blit(text2, (100, 550))

    pygame.display.flip()
    clock.tick(60)
    t = t + 1

pygame.quit()


