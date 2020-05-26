"""utilities.py

Definitions of some functions helpful for drawing UI elements and
performing conversions.
"""

import pygame as pg

from settings import *

# ------------------------------------------------------------------------------

# A Snake_piece and an Apple store their (x, y) coordinates in terms of
# their "tile location". This function converts a tile location to a
# "pixel location" by scaling by the pixels in a tile.
def pixel(n):
    return n * TILE_SIZE

# ------------------------------------------------------------------------------

# A Snake_piece and an Apple are drawn as a dark-coloured outer square
# behind a slightly smaller light square. These functions return the
# corresponding pygame Rect(s).
def outer_rect(square):
    x = pixel(square.x)
    y = pixel(square.y)
    return pg.Rect(x, y, TILE_SIZE, TILE_SIZE)

def inner_rect(square):
    inner_x = pixel(square.x) + TILE_SIZE // 8
    inner_y = pixel(square.y) + TILE_SIZE // 8
    inner_size = int(TILE_SIZE * 0.75)
    return pg.Rect(inner_x, inner_y, inner_size, inner_size)

# ------------------------------------------------------------------------------

def draw_text(surf, text, size=16, x=WIDTH//2, y=HEIGHT//2, color=WHITE):
    font = pg.font.Font("freesansbold.ttf", size)

    text_surf = font.render(text, True, color) # True -> use anti-alias

    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)

    surf.blit(text_surf, text_rect)

# ------------------------------------------------------------------------------

def draw_grid(surf):
    # draw vertical lines
    for x in range(TILE_NUM_X):
        pg.draw.line(surf, GREY, (x * TILE_SIZE, 0),
                     (x * TILE_SIZE, HEIGHT))

    # draw horizontal lines
    for y in range(TILE_NUM_Y):
        pg.draw.line(surf, GREY, (0, y * TILE_SIZE),
                     (WIDTH, y * TILE_SIZE))
