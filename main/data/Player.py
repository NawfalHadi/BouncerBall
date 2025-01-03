import pygame

from main.constant.Size import *
from main.constant.Position import *

class Player():
    def __init__(self, name, x, y, width, height, color, role, side):
        self.name = name
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.speed_x, self.speed_y = 5, -4
        self.color = color
        self.role = role
        self.side = side

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_position(self):
        if self.side == "L":
            self.x += self.role
        elif self.side == "R":
            self.x += FIELD_WIDTH - self.width
            self.x -= self.role