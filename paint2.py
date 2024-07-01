from constant import *
import tkinter as tk
from tkinter import filedialog

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Paint!")
font = pygame.font.SysFont(None, 22)

painting = []

class ImageFromFile:
    def __init__(self, filename):
        self.ma_surface = pygame.image.load(filename)
        self.buf = self.ma_surface.get_buffer()
        self.zoom = 3
        self.x = 0
        self.y = 0
        self.dragging = False

    def paint(self, screen):
        bs = self.ma_surface.get_bytesize()
        for x in range(self.ma_surface.get_width()):
            for y in range(self.ma_surface.get_height()):
                i = (x + y * self.ma_surface.get_width()) * bs
                couleur = (self.buf.raw[i], self.buf.raw[i+1], self.buf.raw[i+2])
                if bs != 4 or self.buf.raw[i+3] != 0:
                    pygame.draw.rect(screen, couleur, [x*self.zoom+self.x, y*self.zoom+100+self.y, self.zoom, self.zoom])

    def isHit(self, pos):
        return pos[0] >= self.x and pos[1] >= self.y+100 \
                and pos[0] <= self.x + self.ma_surface.get_width() * self.zoom \
                and pos[1] <= self.y+100 + self.ma_surface.get_height() * self.zoom

    def startDrag(self, pos):
        if self.isHit(pos):
            self.dragging = True
            print("start drag")
            self.dx = pos[0] - self.x
            self.dy = pos[1] - self.y

    def updateDrag(self, pos):
        if self.dragging:
            self.x = pos[0] - self.dx
            self.y = pos[1] - self.dy

currentImage = ImageFromFile('player.png')


message = ''
display_delay = 0

def actions_btn_1():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    if file_path:
        global currentImage
        painting.append(currentImage)
        currentImage = ImageFromFile(file_path)

def actions_btn_3(pos): # right button
    paints = painting
    for i in range(len(paints)):
        p = paints[i]
        if isinstance(p, ImageFromFile) and p.isHit(pos):
            del paints[i]
            global currentImage
            paints.append(currentImage)
            currentImage = p

def actions_btn_save():
    new_surface = pygame.Surface((WIDTH, HEIGHT))
    new_surface.fill(WHITE)
    paints = painting
    for p in paints:
        if isinstance(p, ImageFromFile):
            p.paint(new_surface)
        else:
            pygame.draw.circle(new_surface, p[0], p[1], p[2])
    i = 0
    filename = 'image.png'
    while os.path.exists(filename):
        i = i + 1
        filename = f'image{i}.png'
    pygame.image.save(new_surface, filename)
    global display_delay, message
    display_delay = 90 # unit is 1/30 s
    message = f"l'image a été sauvée dans {filename}"

def draw_painting(paints):
    for p in paints:
        # pygame.draw.circle(SCREEN, paints[i][0], paints[i][1], paints[i][2])
        if isinstance(p, ImageFromFile):
            p.paint(SCREEN)
        else:
            pygame.draw.circle(SCREEN, p[0], p[1], p[2])
    currentImage.paint(SCREEN)
    global display_delay, message
    if display_delay > 0:
        display_delay = display_delay - 1
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(SCREEN, BLACK, text_rect)
        SCREEN.blit(text, text_rect)

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

    btn_open = pygame.draw.rect(SCREEN, BLUE, [250, 10, 25, 25])
    SCREEN.blit(font.render('Ð', True, WHITE), (252, 20))
    btn_save = pygame.draw.rect(SCREEN, PURPLE, [250, 35, 25, 25])
    SCREEN.blit(font.render('S', True, WHITE), (252, 45))
    btn_list = [btn_open, btn_save]
    for i in range(5):
        btn_list.append(pygame.draw.rect(SCREEN, BLUE, [275+25*i, 10, 25, 25]))
        SCREEN.blit(font.render(str(i+1), True, WHITE), (277+25*i, 20))

    return brush_list, color_rect, rgb_list, btn_list


clock = pygame.time.Clock()
active_size = 20
active_color = BLUE
running = True
while running:
    SCREEN.fill(WHITE)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    draw_painting(painting)
    brushes, colors, rgbs, btns = draw_menu()
    if mouse[1] > 70:
        pygame.draw.circle(SCREEN, active_color, mouse, active_size)
        if left_click:
            painting.append((active_color, mouse, active_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            print (f"middle down {event.pos}")
            currentImage.startDrag(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            print (f"middle button up {event.pos}")
            currentImage.dragging = False
            print("end drag")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            actions_btn_3(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
            for i in range(len(btns)):
                if btns[i].collidepoint(event.pos):
                    if i == 0:
                        actions_btn_1()
                    elif i == 1:
                        actions_btn_save()
                    else:
                        currentImage.zoom = i + (i-2) * 2
        elif event.type == pygame.VIDEORESIZE:
            WIDTH = max(535, event.w)
            HEIGHT = max(350, event.h)
            # There's some code to add back window content here.
            surface = pygame.display.set_mode((WIDTH, HEIGHT),
                                              pygame.RESIZABLE)

    if currentImage.dragging:
        currentImage.updateDrag(pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(os.getcwd())
# os.chdir('C:\\Users\\User\\OneDrive\\Documents\\GoStudent\\21 Vasile_4eme\\novembre\\jeuxpython')
