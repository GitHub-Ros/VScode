# player.py
import pygame

class Player:
    def __init__(self, game):
        self.game = game

    def get_user_choice(self, choices):
        selected_index = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(choices)
                    elif event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(choices)
                    elif event.key == pygame.K_RETURN:
                        return selected_index

            self.game.menu.display_main_menu()  # Fix this line
            self.game.clock.tick(self.game.FPS)
