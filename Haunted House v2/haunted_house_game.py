import pygame
import sys
import time
import menu
from scenario import Scenario
from player import Player
from utilities import TextRenderer, Colors


class HauntedHouseGame:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 30

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Haunted House Adventure")
        self.clock = pygame.time.Clock()

        self.FONT_PATH = "Haunted House v2/assets/Nosifer-Regular.ttf"
        self.BGM_PATH = "Haunted House v2/assets/midnight-123895.mp3"
        self.LINE_SPACING = 40

        self.text_renderer = TextRenderer(self.FONT_PATH, 36)
        self.choices_renderer = TextRenderer(self.FONT_PATH, 20)

        self.menu = menu.Menu(self)
        self.scenario = Scenario(self)
        self.player = Player(self)

        pygame.mixer.music.load(self.BGM_PATH)
        pygame.mixer.music.set_volume(0.5)

    def clear_screen(self):
        self.screen.fill(Colors.BLACK)

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        pygame.mixer.music.play(-1)

        self.scenario.display_scenario("Welcome to the Haunted House Adventure!")

        pygame.display.flip()
        self.clock.tick(self.FPS)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.explore_house()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        self.exit_game()

    def explore_house(self):
        self.scenario.display_scenario("You step inside the dark, dusty foyer.")
        self.scenario.display_scenario("There are three doors in front of you - one to the left, one in the middle, and one to the right.")
        time.sleep(1)

        choices = ["Enter the left door", "Enter the middle door", "Enter the right door", "Go back outside"]
        user_choice = self.player.get_user_choice(choices)

        if user_choice == 0:
            self.explore_left_room()
        elif user_choice == 1:
            self.explore_middle_room()
        elif user_choice == 2:
            self.explore_right_room()
        elif user_choice == 3:
            self.scenario.print_slow("You decide to leave the haunted house. Better safe than sorry!")
            self.exit_game()

    def explore_left_room(self):
        self.scenario.display_scenario("You open the left door and enter a dimly lit room.")
        self.scenario.display_scenario("A ghostly figure appears in front of you!")
        time.sleep(1)

        choices = ["Confront the ghost", "Try to run away"]
        user_choice = self.player.get_user_choice(choices)

        if user_choice == 0:
            self.scenario.print_slow("You try to confront the ghost, but it passes through you, sending chills down your spine.")
            self.game_over("The ghost haunts you forever.")
        elif user_choice == 1:
            self.scenario.print_slow("You try to run away, but the ghost follows you. You can't escape!")
            self.game_over("The ghost catches you, and your vision fades away.")

    def explore_middle_room(self):
        self.scenario.display_scenario("You open the middle door and find a dusty library.")
        self.scenario.display_scenario("A book on the table catches your eye.")
        time.sleep(1)

        choices = ["Read the book", "Ignore the book and leave the room"]
        user_choice = self.player.get_user_choice(choices)

        if user_choice == 0:
            self.scenario.print_slow("As you start reading the book, the words on the pages change to a sinister incantation.")
            self.game_over("You accidentally summon a malevolent spirit.")
        elif user_choice == 1:
            self.scenario.print_slow("You decide to leave the room. The library remains silent.")
            self.explore_house()

    def explore_right_room(self):
        self.scenario.display_scenario("You open the right door and find a dark, mysterious room.")
        self.scenario.display_scenario("A strange, glowing object is on a pedestal in the center.")
        time.sleep(1)

        choices = ["Approach the glowing object", "Leave the room"]
        user_choice = self.player.get_user_choice(choices)

        if user_choice == 0:
            self.scenario.print_slow("As you touch the glowing object, a burst of energy courses through you.")
            self.scenario.print_slow("You feel stronger and more courageous.")
            self.scenario.print_slow("You decide to explore more of the haunted house.")
            self.explore_house()
        elif user_choice == 1:
            self.scenario.print_slow("You decide to leave the room. The glow fades behind you.")
            self.explore_house()

def game_over(self, message):
    self.scenario.display_scenario(message)
    pygame.time.wait(1000)

    replay_text = self.choices_renderer.render_text("Do you want to play again? (Y/N): ", Colors.WHITE, (self.WIDTH // 2, self.HEIGHT // 2 + 50))[0]
    replay_rect = replay_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
    self.screen.blit(replay_text, replay_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    self.menu.display_main_menu()  # Fix method name
                    return
                elif event.key == pygame.K_n:
                    self.scenario.print_slow("Thanks for playing! Goodbye.")
                    self.exit_game()
            elif event.type == pygame.QUIT:
                self.exit_game()


if __name__ == "__main__":
    haunted_house_game = HauntedHouseGame()
    haunted_house_game.start_game()
