from pygame import *
from settings import *
from keys import *
from sounds import *
from sys import *

init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Фортепіано")

BG_COLOR = (0, 0, 0)
BTN_COLOR = (100, 100, 100)
BTN_HOVER = (200, 200, 0)
TEXT_COLOR = (187, 145, 144)

title_font = pygame.font.SysFont("Arial", 40)
btn_font = pygame.font.SysFont("Arial", 24)
info_font = pygame.font.SysFont("Arial", 20)

class Button:

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = BTN_HOVER if self.rect.collidepoint(mouse_pos) else BTN_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius = 6)
        text_surface = btn_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

btn_play = Button("PLAY", 300, 180, 200, 55)
btn_exit = Button("EXIT", 300, 340, 200, 55)

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Fortepiano")

keys_rects = create_keys(len(KEYS))
pressed_keys = set()
sounds = Load_sounds(KEYS)
keys_list = list(KEYS.keys())

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(keys_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)
        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(keys_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)

        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)


    screen.fill(WHITE)
    draw_keys(screen, keys_rects, pressed_keys)
    display.update()

