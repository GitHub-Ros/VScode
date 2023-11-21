import pygame
import sys
import os
from enum import Enum

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 850, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
FONT_PATH = "Haunted House v3/assets/Nosifer-Regular.ttf"
BGM_PATH = "Haunted House v3/assets/midnight-123895.mp3"
# Load and play background music
pygame.mixer.music.load(BGM_PATH)
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Define key constants
KEY_RETURN = pygame.K_RETURN
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haunted House Adventure")

# Define scene enumeration
class Scene(Enum):
    DARK_HALLWAY = 0
    CREAKY_STAIRCASE = 1
    MYSTERIOUS_DOOR = 2
    # ... other scenes ...

# Game variables
current_scene = 0  # or the appropriate enum value
selected_choice = None
current_choice = 0  # Initialize current_choice before using it
in_menu = True

# Define a function to wrap text
def wrap_text(text, width, font):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        if font.size(current_line + word)[0] < width:
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)
    return lines

# Load font with error handling
font_size = 24
try:
    font = pygame.font.Font(FONT_PATH, font_size)
except pygame.error:
    print(f"Error: Font file '{FONT_PATH}' not found.")
    pygame.quit()
    sys.exit()

# Add a variable to track the player's progress in the story
progress = {"portal_opened": False, "ghost_encountered": False, "crystals_touched": False}

# Define scenes and choices
scenes = [
    {"text": "You find yourself in a dark hallway. The air is heavy with an unsettling stillness. What do you do?", "choices": [
        {"text": "Investigate the ominous painting on the wall", "next_scene": 9},
        {"text": "Proceed cautiously down the hallway", "next_scene": 10}
    ]},
    {"text": "You encounter a creaky staircase. The stairs groan beneath each step. How do you proceed?", "choices": [
        {"text": "Ascend the staircase", "next_scene": 11},
        {"text": "Search for another way", "next_scene": 12}
    ]},
    {"text": "A mysterious door stands before you, emanating an ominous energy. What's your decision?", "choices": [
        {"text": "Open the door slowly", "next_scene": 13},
        {"text": "Listen closely for any sounds", "next_scene": 14}
    ]},
    {"text": "You enter a dusty library. The shelves are filled with ancient, decaying books. There's a book on a pedestal. What do you do?", "choices": [
        {"text": "Read the book on the pedestal", "next_scene": 15},
        {"text": "Explore the surrounding bookshelves", "next_scene": 16}
    ]},
    # ... other scenes ...
]

# Extend scenes with more scenes and choices
scenes.extend([
    {"text": "You hear a faint whisper behind you. The words are indistinct, yet haunting. What do you do?", "choices": [
        {"text": "Turn around to investigate", "next_scene": 17},
        {"text": "Ignore the sound and continue forward", "next_scene": 18}
    ]},
    {"text": "A mirror in the hallway reflects an eerie figure. Its eyes seem to follow your every move. How do you react?", "choices": [
        {"text": "Approach the figure in the mirror", "next_scene": 19},
        {"text": "Avoid eye contact and move away", "next_scene": 20}
    ]},
    {"text": "A bone-chilling breeze sweeps through the room. Shadows dance on the walls. What's your next move?", "choices": [
        {"text": "Investigate the source of the breeze", "next_scene": 21},
        {"text": "Find a place to take cover", "next_scene": 22}
    ]},
    {"text": "The lights flicker, and a shadow moves in the corner. A low growl echoes. What's your response?", "choices": [
        {"text": "Confront the shadow head-on", "next_scene": 23},
        {"text": "Retreat to a safer location", "next_scene": 24}
    ]},
    {"text": "You find a locked chest covered in cobwebs. Will you attempt to open it?", "choices": [
        {"text": "Try to open the chest", "next_scene": 25},
        {"text": "Leave the chest undisturbed", "next_scene": 26}
    ]},
    # ... other scenes ...
])

# Add more scenes based on the choices
scenes.extend([
    {"text": "You investigate the sound and discover a skeletal cat. It stares at you with hollow eyes. What do you do?", "choices": [
        {"text": "Offer the cat your hand", "next_scene": 27},
        {"text": "Ignore the cat and continue exploring", "next_scene": 28}
    ]},
    {"text": "The figure in the mirror vanishes, leaving a cold draft. You decide to investigate further...", "choices": [
        {"text": "Search for hidden passages", "next_scene": 29},
        {"text": "Leave the area and return to the hallway", "next_scene": 30}
    ]},
    {"text": "You decide to follow the breeze and find a hidden passage. The walls seem to whisper ancient secrets. Proceed?", "choices": [
        {"text": "Enter the hidden passage", "next_scene": 31},
        {"text": "Stay in the current room", "next_scene": 32}
    ]},
    {"text": "You confront the shadow, only to realize it's a looming specter. Its voice echoes in your mind. What's your next step?", "choices": [
        {"text": "Communicate with the specter", "next_scene": 33},
        {"text": "Flee from the specter", "next_scene": 34}
    ]},
    {"text": "The chest opens with a creak, revealing cursed artifacts. How do you use this malevolent knowledge?", "choices": [
        {"text": "Take the cursed artifacts", "next_scene": 35},
        {"text": "Leave the artifacts undisturbed", "next_scene": 36}
    ]},
])

# Add more scenes based on the second set of choices
scenes.extend([
    {"text": "You decide to adopt the skeletal cat and carry it with you. It emits an otherworldly purr. What's your next move?", "choices": [
        {"text": "Continue your journey with the cat", "next_scene": 37},
        {"text": "Leave the cat and explore alone", "next_scene": 38}
    ]},
    {"text": "You choose to investigate the vanished figure's origins. It leads you to a hidden chamber. What do you find?", "choices": [
        {"text": "Discover the origin of the figure", "next_scene": 39},
        {"text": "Leave the chamber and return to the hallway", "next_scene": 40}
    ]},
    {"text": "You uncover the hidden passage and find a room filled with ghostly treasures. The air feels heavy with lost souls. What's your approach?", "choices": [
        {"text": "Investigate the ghostly treasures", "next_scene": 41},
        {"text": "Leave the room and explore other areas", "next_scene": 42}
    ]},
    {"text": "You embrace your shadow. It morphs into a ghastly guide. It whispers dark secrets. What's your destination?", "choices": [
        {"text": "Follow the shadow guide's advice", "next_scene": 43},
        {"text": "Ignore the shadow guide and proceed on your own", "next_scene": 44}
    ]},
    {"text": "You use the cursed artifacts to unlock a secret door. It leads to a dim-lit crypt. What horrors await within?", "choices": [
        {"text": "Enter the crypt and face the horrors", "next_scene": 45},
        {"text": "Seal the door and avoid the crypt", "next_scene": 46}
    ]},
])
# Add more scenes based on the second set of choices
scenes.extend([
    {"text": "You find a mysterious portal. What will you do?", "choices": [
        {"text": "Enter the portal", "next_scene": 47, "action": lambda: progress.update({"portal_opened": True})},
        {"text": "Ignore the portal", "next_scene": 48}
    ]} if not progress["portal_opened"] else {"text": "The portal shimmers with an otherworldly light. What's your next move?", "choices": [
        {"text": "Step through the portal", "next_scene": 49},
        {"text": "Continue exploring", "next_scene": 50}
    ]},
    {"text": "You encounter a ghostly figure. How do you react?", "choices": [
        {"text": "Communicate with the ghost", "next_scene": 49, "action": lambda: progress.update({"ghost_encountered": True})},
        {"text": "Run away from the ghost", "next_scene": 50}
    ]} if not progress["ghost_encountered"] else {"text": "The ghostly figure recognizes you. What do you want to ask the ghost?", "choices": [
        {"text": "Learn about the ghost's past", "next_scene": 51},
        {"text": "Continue your journey", "next_scene": 52}
    ]},
    {"text": "You discover a room filled with enchanted crystals. What will you do?", "choices": [
        {"text": "Touch the crystals", "next_scene": 53, "action": lambda: progress.update({"crystals_touched": True})},
        {"text": "Leave the room", "next_scene": 54}
    ]} if not progress["crystals_touched"] else {"text": "The crystals resonate with energy. What's your next move?", "choices": [
        {"text": "Channel the crystal's energy", "next_scene": 55},
        {"text": "Proceed cautiously", "next_scene": 56}
    ]},
    # ... Add more scenes and choices based on the player's progress ...
])

# Add more scenes based on the third set of choices
scenes.extend([
    {"text": "You come across a room with a crystal ball. It glows with an eerie light. How will you interact with it?", "choices": [
        {"text": "Peer into the crystal ball", "next_scene": 57},
        {"text": "Leave the room", "next_scene": 58}
    ]},
    {"text": "The crystal ball shows you a vision of the past. What do you see?", "choices": [
        {"text": "A haunting event in the mansion", "next_scene": 59},
        {"text": "Your own past", "next_scene": 60}
    ]},
    {"text": "You find a hidden chamber with ancient artifacts. What will you do with them?", "choices": [
        {"text": "Examine the artifacts closely", "next_scene": 61},
        {"text": "Leave the artifacts untouched", "next_scene": 62}
    ]},
    {"text": "The artifacts reveal a secret passage. Do you enter it or continue exploring?", "choices": [
        {"text": "Enter the secret passage", "next_scene": 63},
        {"text": "Continue exploring the current area", "next_scene": 64}
    ]},
    {"text": "A spectral voice offers guidance. What do you ask the spirit?", "choices": [
        {"text": "Seek guidance on the mansion's history", "next_scene": 65},
        {"text": "Ask about your own destiny", "next_scene": 66}
    ]},
])

# Add more scenes based on the fourth set of choices
scenes.extend([
    {"text": "You find an ancient tome with forbidden knowledge. How do you handle it?", "choices": [
        {"text": "Read the forbidden knowledge", "next_scene": 67},
        {"text": "Close the book and leave the room", "next_scene": 68}
    ]},
    {"text": "The forbidden knowledge grants you supernatural abilities. How will you use them?", "choices": [
        {"text": "Harness the powers for good", "next_scene": 69},
        {"text": "Avoid using the supernatural abilities", "next_scene": 70}
    ]},
    {"text": "You encounter a spectral guardian. What's your approach?", "choices": [
        {"text": "Engage in conversation with the guardian", "next_scene": 71},
        {"text": "Attempt to pass without interacting", "next_scene": 72}
    ]},
    {"text": "The guardian warns of impending danger. How do you prepare?", "choices": [
        {"text": "Gather protective charms", "next_scene": 73},
        {"text": "Disregard the warning and continue", "next_scene": 74}
    ]},
    {"text": "A mysterious figure appears and offers a deal. What's your response?", "choices": [
        {"text": "Accept the mysterious figure's offer", "next_scene": 75},
        {"text": "Decline and continue your journey", "next_scene": 76}
    ]},
])

# Add more scenes based on the fifth set of choices
scenes.extend([
    {"text": "You find yourself in a celestial chamber. What do you perceive in this otherworldly space?", "choices": [
        {"text": "Witness glimpses of the future", "next_scene": 77},
        {"text": "Explore the celestial surroundings", "next_scene": 78}
    ]},
    {"text": "The celestial chamber offers you a glimpse of possible destinies. What path will you choose?", "choices": [
        {"text": "Embrace a heroic destiny", "next_scene": 79},
        {"text": "Forge your own path with free will", "next_scene": 80}
    ]},
    {"text": "You encounter a benevolent spirit. What favor do you ask of the spirit?", "choices": [
        {"text": "Receive guidance for the journey ahead", "next_scene": 81},
        {"text": "Ask for protection from malevolent forces", "next_scene": 82}
    ]},
    {"text": "The benevolent spirit grants you a magical artifact. How will you use its power?", "choices": [
        {"text": "Use the artifact to banish darkness", "next_scene": 83},
        {"text": "Keep the artifact for future challenges", "next_scene": 84}
    ]},
    {"text": "You reach the heart of the haunted mansion. What do you discover in this ominous chamber?", "choices": [
        {"text": "Uncover the mansion's dark secret", "next_scene": 85},
        {"text": "Confront the malevolent force lurking within", "next_scene": 86}
    ]},
])
# Define dynamic descriptions based on player's choices
dynamic_descriptions = {
    53: lambda: "You are drawn to the crystals' glow, feeling a mysterious connection. What will you do?",
    55: lambda: "The crystal's energy surges through you, revealing hidden truths. What's your next move?",
    # ... Add more dynamic descriptions as needed ...
}
# Define a TextBox class for displaying text in a box
class TextBox:
    def __init__(self, text, x, y, width, height, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size

    def update(self, screen):
        lines = wrap_text(self.text, self.width, pygame.font.Font(FONT_PATH, self.font_size))
        text_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i, line in enumerate(lines):
            text_line = font.render(line, True, WHITE)
            text_rect = text_line.get_rect(topleft=(0, i * self.font_size))
            text_surface.blit(text_line, text_rect)

        screen.blit(text_surface, (self.x, self.y))
# Define a DynamicTextBox class for displaying text with dynamic descriptions
class DynamicTextBox:
    def __init__(self, text, x, y, width, height, font_size, dynamic_description):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.dynamic_description = dynamic_description

    def update(self, screen):
        lines = wrap_text(self.text, self.width, pygame.font.Font(FONT_PATH, self.font_size))
        text_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i, line in enumerate(lines):
            text_line = font.render(line, True, WHITE)
            text_rect = text_line.get_rect(topleft=(0, i * self.font_size))
            text_surface.blit(text_line, text_rect)

        # Add dynamic description if available
        if self.dynamic_description:
            dynamic_text = self.dynamic_description()
            dynamic_lines = wrap_text(dynamic_text, self.width, pygame.font.Font(FONT_PATH, self.font_size))
            for i, line in enumerate(dynamic_lines):
                dynamic_line = font.render(line, True, WHITE)
                dynamic_rect = dynamic_line.get_rect(topleft=(0, (len(lines) + i) * self.font_size))
                text_surface.blit(dynamic_line, dynamic_rect)

        screen.blit(text_surface, (self.x, self.y))


# Define a ChoiceBox class for displaying choices in a box
class ChoiceBox:
    def __init__(self, choices, x, y, width, height, font_size):
        self.choices = choices
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size

    def update(self, screen, selected_choice):
        for i, choice in enumerate(self.choices):
            choice_text = f"{i + 1}. {choice['text']}"
            choice_color = WHITE if i == selected_choice else RED
            lines = wrap_text(choice_text, self.width, pygame.font.Font(FONT_PATH, self.font_size))
            text_surface = pygame.Surface((self.width, self.height // len(self.choices)), pygame.SRCALPHA)
            for j, line in enumerate(lines):
                text_line = font.render(line, True, choice_color)
                text_rect = text_line.get_rect(topleft=(0, j * self.font_size))
                text_surface.blit(text_line, text_rect)

            screen.blit(text_surface, (self.x, self.y + i * (self.height // len(self.choices))))

# Create a clock object
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if in_menu and event.key == pygame.K_RETURN:
                in_menu = False
            elif not in_menu:
                if event.key == pygame.K_UP:
                    current_choice = (current_choice - 1) % len(scenes[current_scene]["choices"])
                elif event.key == pygame.K_DOWN:
                    current_choice = (current_choice + 1) % len(scenes[current_scene]["choices"])
                elif event.key == pygame.K_RETURN and len(scenes[current_scene]["choices"]) > 0:
                    selected_choice = current_choice

    screen.fill(BLACK)

    if in_menu:
        # Display main menu text
        title_text = font.render("Haunted House Adventure", True, WHITE)
        start_text = font.render("Press Enter to start", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
    else:
        # Display the current scene text with dynamic descriptions
        dynamic_description = dynamic_descriptions.get(current_scene, None)
        text_box = DynamicTextBox(scenes[current_scene]["text"], 60, (HEIGHT - 200) // 4, WIDTH - 120, 200, font_size, dynamic_description)
        text_box.update(screen)

        # Display the choices in a separate box
        max_choice_height = (HEIGHT - 200) // 2
        available_height = max_choice_height - 40
        font_size_choice = min(24, available_height // len(scenes[current_scene]["choices"]))
        choice_box = ChoiceBox(scenes[current_scene]["choices"], 60, (HEIGHT - 200) // 2, WIDTH - 120, max_choice_height, font_size_choice)
        choice_box.update(screen, current_choice)

    pygame.display.flip()
    if selected_choice is not None:
        # Update progress if there is an associated action
        action = scenes[current_scene]["choices"][selected_choice].get("action", None)
        if action:
            action()

        if "choices" in scenes[current_scene]:
            current_scene = scenes[current_scene]["choices"][selected_choice]["next_scene"]
            selected_choice = None
            print("Current Scene:", current_scene)
        else:
            print("No choices in the current scene")
    clock.tick(30)
