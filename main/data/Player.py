import pygame

from main.constant.Size import *
from main.constant.Position import *
from main.constant.Color import *

class Player():
    def __init__(self, name, x, y, width, height, color, role, side, number=0, path=None):
        self.name = name
        self.x, self.y = x, y
        self.color = color
        self.side = side

        "== ATTRIBUTE =="
        self.name = name
        self.number = number
        self.width, self.height = width, height

        "== STATS =="
        self.speed_x, self.speed_y = 5, -4

        "== MOVEMENT =="
        self.role = role
        self.path = path

        "== STATE =="
        self.isStartMove = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 18)
        text = font.render(str(self.number), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)
        
    def set_position(self):
        if self.side == "L":
            self.x = START_FIELD_WIDHT + self.x
            self.y = START_FIELD_HEIGHT + self.y
        elif self.side == "R":
            self.x += FIELD_WIDTH - self.width
            self.x -= self.role

    def get_names(self, screen):
        cursor_pos = pygame.mouse.get_pos()
        
        rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if rect.collidepoint(cursor_pos):
            font = pygame.font.Font(None, 18)
            text = font.render(self.name, True, (BLACK))
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height + 10))
            screen.blit(text, text_rect)