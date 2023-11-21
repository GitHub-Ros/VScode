# main.py
import haunted_house_game
import menu

def main():
    game_instance = haunted_house_game.HauntedHouseGame()  # Create an instance of the HauntedHouseGame class

    # Display main menu
    game_instance.menu.display_main_menu()
    game_instance.menu.wait_for_start()

    # Start the game
    game_instance.start_game()

if __name__ == "__main__":
    main()
