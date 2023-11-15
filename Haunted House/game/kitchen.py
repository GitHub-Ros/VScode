# game/kitchen.py
from game.room import Room

def enter_kitchen():
    kitchen = Room(
        name="Kitchen",
        description="You step into the chilling kitchen. Broken dishes are scattered on the floor. "
                    "The flickering light casts long, distorted shadows, and a faint, distant moan echoes through the room."
    )

    dining_room = Room(
        name="Dining Room",
        description="The dining room is dimly lit, and a long table dominates the center. "
                    "An unsettling silence hangs in the air, broken only by the occasional creaking of the floorboards."
    )

    garden = Room(
        name="Garden",
        description="You find yourself in an overgrown garden. Thorny bushes block the way. "
                    "The moonlight casts eerie shadows, and the rustling of unseen creatures adds to the unsettling atmosphere."
    )

    kitchen.connect_rooms(dining_room, 'east')
    kitchen.connect_rooms(garden, 'west')

    current_room = kitchen
    while True:
        current_room.describe_room()
        current_room.list_connected_rooms()

        choice = input("What do you want to do? (1. Investigate the broken dishes / 2. Go back): ")
        if choice == '1':
            investigate_dishes()
        elif choice == '2':
            return
        else:
            print("Invalid choice. Try again.")

def investigate_dishes():
    print("You carefully inspect the broken dishes, revealing a hidden trapdoor.")
    # Implement logic for discovering a trapdoor
