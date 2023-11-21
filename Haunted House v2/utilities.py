# In utilities.py
import pygame

class TextRenderer:
    def __init__(self, font_path, font_size):
        self.font = pygame.font.Font(font_path, font_size)

    def render_text(self, text, color, position):
        rendered_text = self.font.render(text, True, color)
        text_rect = rendered_text.get_rect(topleft=position)
        return rendered_text, text_rect


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SCENARIO_COLOR = (150, 50, 50)  # Adjusted spooky color
    HIGHLIGHT_COLOR = (255, 255, 0)
