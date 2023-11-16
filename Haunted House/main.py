# main.py
from game.hall import enter_hall, start_game

def play_menu():
    print("Welcome to the Horror Adventure Game!")
    print("1. Play")
    print("2. About")
    print("3. Exit")

def about_menu():
    print("--------------------------------")
    print("About the Horror Adventure Game:")
    print("--------------------------------")
    print("This is a text-based horror adventure game where you explore a mysterious mansion.")
    print("Your choices will determine your fate. Good luck!")
    print("--------------------------------")


def main():
    while True:
        play_menu()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            start_game()
            enter_hall()  # Start the game
        elif choice == '2':
            about_menu()  # Display information about the game
        elif choice == '3':
            print("Exiting the Horror Adventure Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
