import pygame

WIDTH =390
HEIGHT = 844
FPS = 30

BLACK = (0, 0, 0)
BG_GREY = (188, 188, 188)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kolesiki")
clock = pygame.time.Clock()


# Текстовое поле
class Canvas():
    def __init__(self, size, image, surf):
        self.surf = surf
        self.canvas = pygame.image.load(image)
        self.canvas_rect = self.canvas.get_rect(center=(size[0]/2, size[1]/2))


    def create(self):
        self.surf.blit(self.canvas, self.canvas_rect)

    
    def output(self, text, rect):
        self.surf.blit(text, rect)


# Кнопка 
class Button():
    def __init__(self, image, pos):
        self.image = image
        self.pos = pos
        self.button = pygame.image.load(image)
        self.button_rect = self.button.get_rect(center=pos)

    
    # Проверка на перечечение с кнопкой 
    def collision(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            return True


    # Вывод на экран
    def draw(self, surf):
        surf.blit(self.button, self.button_rect)


canvas_big = Canvas((390, 88), 'assets/canvas_big.png', screen)

canvas_blured = Canvas((WIDTH, HEIGHT), 'assets/canvas_blured.png', screen)

buttons = {'button_yellow.png': (WIDTH/2, 200), 'button_green.png': (WIDTH/2, 350), 
           'button_blue.png': (WIDTH/2, 500), 'button_pink.png': (WIDTH/2, 650)}

buttons_pressed = {'button_yellow_p.png': (WIDTH/2, 200), 'button_green_p.png': (WIDTH/2, 350), 
                   'button_blue_p.png': (WIDTH/2, 500), 'button_pink_p.png': (WIDTH/2, 650)}

canvases_small_buttons = [(WIDTH/2, 150), (WIDTH/2, 300), (WIDTH/2, 450), (WIDTH/2, 600)]

crossButton = Button('assets/cross.png', (25, 25))
crossButton_p = Button('assets/cross_p.png', (25, 25))

btns = list()
btns_p = list()
cnvs = list()

for k, v in buttons.items():
    btns.append(Button('assets/' + k, v))

for k1, v1 in buttons_pressed.items():
    btns_p.append(Button('assets/' + k1, v1))

for x in canvases_small_buttons:
    cnvs.append(Button('assets/canvas_small.png', x))

isOpen = True
wasPressed = False
canvasPressed = False

while isOpen:
    screen.fill(BG_GREY)
    canvas_big.create()

    for i, y in zip(btns, cnvs):
        i.draw(screen)
        y.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isOpen = False
        elif event.type == pygame.MOUSEBUTTONUP:
            wasPressed = False

    for a, b, c in zip(btns, btns_p, cnvs):
        if pygame.mouse.get_pressed()[0] and a.collision():
            b.draw(screen)
            wasPressed = True
        elif pygame.mouse.get_pressed()[0] and c.collision():
            canvasPressed = True

    if canvasPressed:
        canvas_blured.create()
        crossButton.draw(screen)

        if pygame.mouse.get_pressed()[0] and crossButton.collision():
            crossButton_p.draw(screen)

            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    canvasPressed = False
                    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()