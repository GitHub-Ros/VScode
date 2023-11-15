# game/hall.py
from game.room import Room

def enter_hall():
    hall = Room(
        name="Grand Hall",
        description="Dim moonlight barely illuminates the faded portraits on the walls, their eyes seemingly following your every move. "
                    "Your arms feel heavy. Your knees feel weak and you are acutely aware of the condensation on your palms."
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

    # Adding an interactive object in the hall
    hall.objects["candle"] = "A flickering candle on a dusty table."

    hall.connect_rooms(kitchen, 'north')
    hall.connect_rooms(dining_room, 'east')
    hall.connect_rooms(garden, 'west')

    current_room = hall
    while True:
        current_room.describe_room()
        current_room.list_connected_rooms()

        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in ['north', 'south', 'east', 'west']:
            current_room = current_room.move(direction)
        else:
            print("Invalid direction. Try again.")
