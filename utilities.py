import pygame as pg

from settings import *

# ------------------------------------------------------------------------------

# A Snake_piece and an Apple store their (x, y) coordinates in terms of
# their "tile location". This function converts a tile location to a
# "pixel location" by scaling by the pixels in a tile.
def pixel(n):
    return n * TILE_SIZE

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
