import pygame

class Ball:
    def __init__(self, x, y):
        self.image = pygame.image.load("main/assets/balls.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.width, self.height = self.image.get_width(), self.image.get_height()
        
        self.x, self.y = x, y
        self.speed_x, self.speed_y = 7, 5
        self.friction = 0.99
        self.min_speed = 0.5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))