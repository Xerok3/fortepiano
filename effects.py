from pygame import *
from settings import *

def draw_key_effects(screen, rect, is_pressed = False):
    if not is_pressed:
        base_color = (227, 217, 198)
    else:
        base_color = (230, 210, 181)

    border_color = BLACK
    draw.rect(screen, base_color, rect, border_radius=8)
    draw.rect(screen, border_color, rect, 2, border_radius=8)