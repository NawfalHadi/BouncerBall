import pygame

from main.constant.Color import *

class InputText:
    def __init__(self, x, y, width, height, color_inactive, color_active, max_text = 100, text=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = color_inactive
        self.text = text if text else ""
        self.max_text = max_text
        self.isActive = False

    def draw(self, screen):
        font = pygame.font.Font(None, 32)

        txt_surface = font.render(self.text, True, BLACK)
        self.rect.w = self.rect.width

        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def activate_input(self):
        cursor_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(cursor_pos):
            self.color = self.color_active
        else:
            self.color = self.color_inactive

    def check_input(self):
        if self.text:
            if len(self.text) == self.max_text:
                self.isActive = False
            elif len(self.text) < self.max_text:
                self.isActive = True