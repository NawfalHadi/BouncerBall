import pygame

from main.constant.Color import *

class TextBox:
    def __init__(self, text, x, y, widht, height, color=BLACK, font_color=WHITE, font_size = 24):
        self.text = text
        self.rect = pygame.Rect(x, y, widht, height)
        self.color = color
        self.font_color = font_color
        self.font_size = font_size

    def draw(self, screen):
        font = pygame.font.Font(None, self.font_size)

        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, self.font_color)

        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)