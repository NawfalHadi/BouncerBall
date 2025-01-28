import pygame

class Schedule():
    def __init__(self, home_team, away_team, home_score, away_score, finish=False):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.isFinish = finish

    def set_rectangle(self, x, y, widht, height, font_color, font_hover, color, color_hover, action=None):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, widht, height)
        self.font_color = font_color
        self.font_hover = font_hover
        self.color = color
        self.color_hover = color_hover
        self.action = action

    def draw(self, screen, margin_team_name):
        font = pygame.font.Font(None, 36)

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.color_hover, self.rect)
            home_name = font.render(self.home_team.name, True, self.font_hover)
            away_name = font.render(self.away_team.name, True, self.font_hover)
            text_score = font.render(f"{self.home_score} VS {self.away_score}", True, self.font_hover)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            home_name = font.render(self.home_team.name, True, self.font_color)
            away_name = font.render(self.away_team.name, True, self.font_color)
            text_score = font.render(f"{self.home_score} VS {self.away_score}", True, self.font_color)            

        " == HOME TEAM INFORMATION =="
        left_rect = pygame.Rect(self.x + 20, self.y + 10, 20, 20)
        pygame.draw.rect(screen, self.home_team.color, left_rect)

        screen.blit(home_name, (self.rect.x + 50, self.rect.y + 10))
        screen.blit(text_score, (left_rect.right + margin_team_name + 20, self.rect.y + 10))

        " == AWAY TEAM INFORMATION =="
        screen.blit(away_name, (left_rect.right + margin_team_name + text_score.get_rect().right + 50, self.rect.y + 10))
        
        right_rect = pygame.Rect(left_rect.right + margin_team_name + text_score.get_rect().right + away_name.get_rect().right + 70, self.y + 10, 20, 20)
        pygame.draw.rect(screen, self.away_team.color, right_rect)


        
