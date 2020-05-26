import pygame as pg

from settings import *
from sprite import *
from utilities import *

# ------------------------------------------------------------------------------

class Display_window:
    """Controls the window that appears on the player's screen when
    they run main.py."""

    def __init__(self, caption):
        self.screen = pg.display.set_mode(WINDOW_AREA)
        self.open = True
        pg.display.set_caption(caption)

    def is_open(self):
        return self.open

    def close(self):
        self.open = False

# ------------------------------------------------------------------------------

class Game:
    """Controls the main game loop (detect input events, update sprite
    attributes, draw sprites on screen)."""

    def __init__(self):
        self.display_window = Display_window("Snake")
        self.clock = pg.time.Clock()

    def reset(self):
        """Called before run() to put the Game in its start state."""
        self.score = 0
        self.snake = Snake()
        self.apple = Apple()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                self.snake.set_direction(event.key)

    def update(self):
        # Might have quit() just before this in events(). User also might not
        # have pressed a key yet.
        if not self.running or not self.snake.is_moving():
            return

        self.snake.update()

        if did_collide(self.snake, self.apple):
            self.apple.update(self.snake.body())
            self.score += 10
        else:
            self.snake.update_tail()

        if not self.snake.head().is_on_screen():
            self.running = False

        if hit_own_body(self.snake):
            self.running = False

    def draw(self, surf):
        surf.fill(BLACK)
        self.snake.draw(surf)
        self.apple.draw(surf)
        draw_grid(surf)
        draw_text(surf, "Score: " + str(self.score), y=20)

    def run(self):
        """The main loop."""
        self.running = True # eventually will be set False in update()
        while self.running:
            self.events()
            self.update()
            self.draw(self.display_window.screen)
            pg.display.update()
            self.clock.tick(FPS)

    def quit(self):
        """Called when the player closes the display window."""
        self.running = False
        self.display_window.close()
