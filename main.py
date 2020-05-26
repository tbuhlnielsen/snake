"""Snake

A clone of the classic game. Move with the arrow keys or W, A, S, D.

~To do~
* Start and end screens.

~History~
First written: 24th Feb 2020
Refactored: 24th May 2020
"""

import pygame as pg

from game import *
from settings import *

# ------------------------------------------------------------------------------

def main():
    # load pygame modules
    pg.init()

    # check settings
    assert WIDTH % TILE_SIZE == 0, "WIDTH must be a multiple of TILE_SIZE"
    assert HEIGHT % TILE_SIZE == 0, "HEIGHT must be a multiple of TILE_SIZE"

    snake = Game()
    # show_start_screen(snake) # TO DO
    while snake.display_window.is_open:
        snake.reset()
        snake.run()
        # show_end_screen(snake) # TO DO

    pg.quit()

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
