# main.py

from game.hall import enter_hall
# intro
def start_game():
    print(">You slowly regain consciousness, disoriented and surrounded by darkness")
    print(">As your eyes adjust, you find yourself standing in the grand hall of an old decrepit mansion.")
    print(">The air is thick with an eerie stillness, broken only by distant creaks and faint whispers.")
    print(">A chilling sensation runs down your spine as you realize you have no memory of how you got here.")
    print(">Determined to unravel the mystery surrounding you, you take a deep breath and decide to explore the house.")

    enter_hall()

if __name__=="__main__":
    start_game()