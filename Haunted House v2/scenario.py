# In scenario.py
import pygame
import time
from utilities import TextRenderer, Colors

class Scenario:
    def __init__(self, game):
        self.game = game

    def display_scenario(self, text, highlighted=False):
        self.game.clear_screen()

        # Center the text
        rendered_text, text_rect = self.game.text_renderer.render_text(
            text, Colors.HIGHLIGHT_COLOR if highlighted else Colors.SCENARIO_COLOR,
            (self.game.WIDTH // 2, self.game.HEIGHT // 2)
        )
        text_rect.center = (self.game.WIDTH // 2, self.game.HEIGHT // 2)

        # Display the text
        self.game.screen.blit(rendered_text, text_rect)
        pygame.display.flip()

        # Wait for a moment before returning to the main loop
        pygame.time.wait(2000)
