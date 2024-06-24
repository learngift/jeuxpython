from constant import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint!")

painting = []

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(SCREEN, paints[i][0], paints[i][1], paints[i][2])

def draw_menu():
    pygame.draw.rect(SCREEN, GREY, [0, 0, WIDTH, 70])
    pygame.draw.line(SCREEN, BLACK, (0, 70), (WIDTH, 70), 3)
    xl_brush = pygame.draw.rect(SCREEN, BLACK, [10, 10, 50, 50])
    pygame.draw.circle(SCREEN, WHITE, (35, 35), 20)
    l_brush = pygame.draw.rect(SCREEN, BLACK, [70, 10, 50, 50])
    pygame.draw.circle(SCREEN, WHITE, (95, 35), 15)
    m_brush = pygame.draw.rect(SCREEN, BLACK, [130, 10, 50, 50])
    pygame.draw.circle(SCREEN, WHITE, (155, 35), 10)
    s_brush = pygame.draw.rect(SCREEN, BLACK, [190, 10, 50, 50])
    pygame.draw.circle(SCREEN, WHITE, (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    blue   = pygame.draw.rect(SCREEN, BLUE,   [WIDTH-35,  10, 25, 25])
    red    = pygame.draw.rect(SCREEN, RED,    [WIDTH-35,  35, 25, 25])
    green  = pygame.draw.rect(SCREEN, GREEN,  [WIDTH-60,  10, 25, 25])
    yellow = pygame.draw.rect(SCREEN, YELLOW, [WIDTH-60,  35, 25, 25])
    teal   = pygame.draw.rect(SCREEN, TEAL,   [WIDTH-85,  10, 25, 25])
    purple = pygame.draw.rect(SCREEN, PURPLE, [WIDTH-85,  35, 25, 25])
    orange = pygame.draw.rect(SCREEN, ORANGE, [WIDTH-110, 10, 25, 25])
    grey   = pygame.draw.rect(SCREEN, GREY,   [WIDTH-110, 35, 25, 25])
    white  = pygame.draw.rect(SCREEN, WHITE,  [WIDTH-135, 10, 25, 25])
    black  = pygame.draw.rect(SCREEN, BLACK,  [WIDTH-135, 35, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, orange, grey, white, black]
    rgb_list   = [BLUE, RED, GREEN, YELLOW, TEAL, PURPLE, ORANGE, GREY, WHITE, BLACK]
    return brush_list, color_rect, rgb_list


clock = pygame.time.Clock()
active_size = 20
active_color = BLUE
running = True
while running:
    SCREEN.fill(WHITE)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    draw_painting(painting)
    brushes, colors, rgbs = draw_menu()
    if mouse[1] > 70:
        pygame.draw.circle(SCREEN, active_color, mouse, active_size)
        if left_click:
            painting.append((active_color, mouse, active_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()