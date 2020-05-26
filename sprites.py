import pygame as pg

from random import randint

from settings import *
from utilities import *

# ------------------------------------------------------------------------------

class Sprite_square:
    """Represents a square in the grid that is occupied by either a piece
    of a Snake or an Apple; both have (x, y) coordinates and are drawn as
    a dark-coloured outer square behind a slightly smaller light square.

    x and y represent the tile location of a Sprite_square; to get the pixel
    location we use pixel(), which is defined in utilities.py."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_screen(self):
        """Used to end the game if a Snake goes off the screen."""
        if pixel(self.x) < 0 or WIDTH - TILE_SIZE < pixel(self.x):
            return False

        if pixel(self.y) < 0 or HEIGHT - TILE_SIZE < pixel(self.y):
            return False

        return True

    def draw(self, surf, inner_color, outer_color):
        pg.draw.rect(surf, outer_color, outer_rect(self))
        pg.draw.rect(surf, inner_color, inner_rect(self))

def outer_rect(square):
    """Returns a pygame Rect the size of a tile in the grid."""
    x = pixel(square.x)
    y = pixel(square.y)
    return pg.Rect(x, y, TILE_SIZE, TILE_SIZE)

def inner_rect(square):
    """Returns a pygame Rect slightly smaller than a tile in the grid."""
    inner_x = pixel(square.x) + TILE_SIZE // 8
    inner_y = pixel(square.y) + TILE_SIZE // 8
    inner_size = int(TILE_SIZE * 0.75)
    return pg.Rect(inner_x, inner_y, inner_size, inner_size)

# ------------------------------------------------------------------------------

class Snake:
    """An array of Sprite_square(s); the head is the square at index 0
    and the tail is the square at index -1.

    The main two functions responsible for achieving the snake-like
    movement effect are update() and update_tail().

    The idea is to insert a new Sprite_square in front of the head every
    frame (where the meaning of "in front of" is determined by the
    direction the Snake is currently travelling in). This is done by
    update(). Then, unless the head has just hit an Apple, the tail is
    removed from the array to keep the length of the array constant.
    This is done by update_tail()."""

    def __init__(self, x0=3, y0=3):
        # Start with three pieces aligned horizontally.
        self.pieces = [Sprite_square(x0-i, y0) for i in range(3)]
        self.direction = None # Will be set when a key is pressed.

    def head(self):
        return self.pieces[0]

    def body(self, initial=0):
        """Returns a list of (x, y) coordinates for each piece of a
        Snake, starting from the piece at index initial. Used by
        Apple.update() and hit_own_body()."""
        return self.pieces[initial:]

    def is_moving(self):
        return self.direction

    def set_direction(self, key):
        if key in [pg.K_UP, pg.K_w] and self.direction != DOWN:
            self.direction = UP
        elif key in [pg.K_DOWN, pg.K_s] and self.direction != UP:
            self.direction = DOWN
        elif key in [pg.K_LEFT, pg.K_a] and self.direction != RIGHT:
            self.direction = LEFT
        elif key in [pg.K_RIGHT, pg.K_d] and self.direction != LEFT:
            self.direction = RIGHT

    def update_tail(self):
        self.pieces.pop()

    def update(self):
        x, y = self.head().x, self.head().y

        if self.direction == UP:
            y -= 1
        elif self.direction == DOWN:
            y += 1
        elif self.direction == LEFT:
            x -= 1
        elif self.direction == RIGHT:
            x += 1

        self.pieces.insert(0, Sprite_square(x, y))

    def draw(self, surf):
        for piece in self.pieces:
            piece.draw(surf, GREEN, DARK_GREEN)

# ------------------------------------------------------------------------------

class Apple(Sprite_square):

    def __init__(self, x=6, y=3):
        super().__init__(x, y)
        self.locations = []

    def update(self, snake_body):
        """Moves an Apple to a grid square it hasn't been in before."""
        square = Sprite_square(*get_random_coords())
        while square in self.locations or square in snake_body:
            square.x, square.y = get_random_coords()

        self.x, self.y = square.x, square.y
        self.locations.append(square)

    def draw(self, surf):
        super().draw(surf, RED, DARK_RED)

# ------------------------------------------------------------------------------

def get_random_coords():
    x = randint(0, TILE_NUM_X - 1) # Closed interval.
    y = randint(0, TILE_NUM_Y - 1)
    return x, y

def did_collide(snake, apple):
    return snake.head().x == apple.x and snake.head().y == apple.y

def hit_own_body(snake):
    for square in snake.body(1):
        if square == snake.head():
            return True
    return False
