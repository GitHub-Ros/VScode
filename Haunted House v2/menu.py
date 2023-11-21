# menu.py
import pygame
from utilities import *

class Menu:
    def __init__(self, game):
        self.game = game

    def display_main_menu(self):
        title_text = "Haunted House Adventure"
        start_text = "Press ENTER to start"

        # Clear the screen
        self.game.clear_screen()

        # Display title
        title_font = pygame.font.Font(self.game.FONT_PATH, 48)
        title_rendered_text = title_font.render(title_text, True, Colors.WHITE)
        title_text_rect = title_rendered_text.get_rect(center=(self.game.WIDTH // 2, self.game.HEIGHT // 3))
        self.game.screen.blit(title_rendered_text, title_text_rect)

        # Display start prompt
        start_font = pygame.font.Font(self.game.FONT_PATH, 24)
        start_rendered_text = start_font.render(start_text, True, Colors.HIGHLIGHT_COLOR)
        start_text_rect = start_rendered_text.get_rect(center=(self.game.WIDTH // 2, 2 * self.game.HEIGHT // 3))
        self.game.screen.blit(start_rendered_text, start_text_rect)

        pygame.display.flip()  # Update the display
        self.game.clock.tick(self.game.FPS)  # Control the frame rate

    def wait_for_start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            self.display_main_menu()
