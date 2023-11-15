# game/room.py

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.objects = {}
        self.visited = False  # New attribute to track whether the room has been visited

    def connect_rooms(self, other_room, direction):
        self.connected_rooms[direction] = other_room

    def describe_room(self):
        if not self.visited:
            print(f"\nYou are in the {self.name}. {self.description}")

            if self.objects:
                print("\nYou notice the following objects:")
                for obj_name, obj_description in self.objects.items():
                    print(f"- {obj_name}: {obj_description}")

            self.visited = True
        else:
            print(f"\nYou are back in the {self.name}.")

    def list_connected_rooms(self):
        print("\nFrom here, you can go to:")
        for direction, room in self.connected_rooms.items():
            print(f"- {direction.capitalize()}: {room.name}")

    def move(self, direction):
        if direction in self.connected_rooms:
            return self.connected_rooms[direction]
        else:
            print("You can't go that way.")
            return self