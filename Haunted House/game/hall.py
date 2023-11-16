# game/hall.py
from game.room import Room

def start_game():
    print("# You slowly regain consciousness, disoriented and surrounded by darkness.")
    print("# As your eyes adjust, you find yourself standing in the grand hall of an old decrepit mansion.")
    print("# The air is thick with an eerie stillness, broken only by distant creaks and faint whispers.")
    print("# A chilling sensation runs down your spine as you realize you have no memory of how you got here.")
    print("# Determined to unravel the mystery surrounding you, you take a deep breath and decide to explore the house.")

def enter_hall():
    hall = Room(
        name="Grand Hall",
        description="Dim moonlight barely illuminates the faded portraits on the walls, their eyes seemingly following your every move. "
                    "Your arms feel heavy. Your knees feel weak, and you are acutely aware of the condensation on your palms."
    )

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

    # Adding interactive objects in the hall
    hall.objects["candle"] = "A flickering candle on a dusty table."
    hall.objects["note"] = "A crumpled piece of paper with cryptic writing."

    hall.connect_rooms(kitchen, 'north')
    hall.connect_rooms(dining_room, 'east')
    hall.connect_rooms(garden, 'west')

    current_room = hall
    note_found = False  # Keep track of whether the note has been found

    while True:
        current_room.describe_room()

        print("\nActions you can perform:")
        print("1. Examine the candle")
        print("2. Investigate the portraits")
        print("3. Move to another room")

        if not note_found and current_room.name == "Grand Hall":
            print("4. Examine the crumpled piece of paper")

        action_choice = input("What do you want to do? (Enter the number of your choice): ")
        if action_choice == '1':
            print("\n>You examine the flickering candle. It seems ordinary, but its light dances eerily in the hall.")
        elif action_choice == '2':
            print("\n>You closely inspect the faded portraits on the walls. Their eyes follow your every move, creating an unsettling feeling.")
        elif action_choice == '3':
            print("\n>You consider moving to another room.")
            room_options = current_room.list_connected_rooms()
            print("\nAvailable Rooms:")
            for i, (_, room) in enumerate(room_options, start=1):
                print(f"{i}. Move to the {room.name}")

            room_choice = input("Enter the number of your choice (or '0' to stay in the current room): ")
            if room_choice.isdigit() and 1 <= int(room_choice) <= len(room_options):
                _, next_room = room_options[int(room_choice) - 1]
                current_room = next_room
                print(f"\n>You decide to move to the {current_room.name}.")
            elif room_choice == '0':
                print(f"\n>You decide to stay in the {current_room.name}.")
            else:
                print("Invalid choice. Try again.")
        elif action_choice == '4' and not note_found and current_room.name == "Grand Hall":
            print("\n>You find a crumpled piece of paper on the floor. The writing is cryptic and unsettling:")
            print("\n>'Beware the shadows that dance in the moonlight. Seek the three keys, but know this – the mansion harbors a cosmic secret, "
                  "and an otherworldly entity awaits your awakening. Madness may be your only escape.'")
            note_found = True
        else:
            print("Invalid choice. Try again.")
