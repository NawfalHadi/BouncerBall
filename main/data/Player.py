import pygame

class Player():
    def __init__(self, name, x, y, width, height, color):
        self.player_x, self.player_y = x, y
        self.player_width, self.player_height = width, height
        self.player_speed_x, self.player_speed_y = 5, -4
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.player_x, self.player_y, self.player_width, self.player_height))