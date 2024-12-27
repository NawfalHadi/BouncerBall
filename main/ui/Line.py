import pygame

class Line:
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.p1, self.p2, 2)

    def get_rect(self):
        return pygame.Rect(self.p1, self.p2)
    
    def get_coor(self):
        rect = self.get_rect()

        top = rect.top
        left = rect.left
        bottom = rect.bottom
        right = rect.right

        return top, left, bottom, right