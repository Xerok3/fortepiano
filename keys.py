from pygame import *
from effects import *

def create_keys(num_keys, start_x = 50, start_y = 200, key_width = 100, key_height = 325):
    rects = []
    for i in range(num_keys):
        x = start_x + i * key_width
        rects.append(Rect(x, start_y, key_width, key_height))
    return rects

def draw_keys(screen, key_rects, pressed_key):
    for i, rect in enumerate(key_rects):
        is_pressed = i in pressed_key
        draw_key_effects(screen, rect, is_pressed)