import pygame

from main.constant.Size import *
from main.constant.Color import *

from main.ui.Line import Line
from main.ui.Button import Button

class CreateTeamsPage:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Create Teams")

        "== PAGE STATE =="
        self.isLoading = True
        self.isRunning = True

        "== PLAYER =="
        self.players = []
        self.player_mark = None
        self.player_direction = 0
        self.player_position = None
        self.player_number = 0
        self.player_name = None

        "== STATE =="
        self.isPlayerMarking = False
        self.isPlayerDirected = False
        self.isPlayerHasRole = False
        self.isPlayerHasNumber = False
        self.isPlayerHasName = False

        "== INTERFACE =="
        self.text_explanation = "Click on the field to mark player spots"

        self.init_field()

    "== INTERFACE =="
    def update_title(self):
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text_explanation, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=(SCREEN_WIDTH // 2, START_FIELD_HEIGHT - 50))
        self.screen.blit(self.text_surface, self.text_rect)

    "== FIELD =="

    def init_field(self):
        self.left_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.top_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), BLACK)
        self.bottom_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_left_field = Line((START_FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_GK_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_left_field = Line((START_FIELD_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_left_vertical = Line((START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

        self.center_field = Line((START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

    def draw_field(self):
        self.left_field.draw(self.screen)
        self.right_field.draw(self.screen)
        self.top_field.draw(self.screen)
        self.bottom_field.draw(self.screen)

        self.top_gk_left_field.draw(self.screen)
        self.bottom_gk_left_field.draw(self.screen)
        self.gk_left_vertical.draw(self.screen)

        self.center_field.draw(self.screen)
        self.center_circle = pygame.draw.circle(self.screen, BLACK, (START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2), 73, 2)


        self.top_gk_right_field.draw(self.screen)
        self.bottom_gk_right_field.draw(self.screen)
        self.gk_right_vertical.draw(self.screen)

    "== MARKING =="
    def mark_player_spot(self, pos):
        x, y = pos
        if START_FIELD_WIDHT <= x <= START_FIELD_WIDHT + FIELD_WIDTH and START_FIELD_HEIGHT <= y <= START_FIELD_HEIGHT + FIELD_HEIGHT:
            self.text_explanation = "Choose the player direction when games start \nEsc to cancel"
            self.player_mark = pygame.Rect(x - 25, y - 25, 40, 40)
            self.isPlayerMarking = True

    def draw_player_spot(self):
        if self.player_mark:
            pygame.draw.rect(self.screen, RED, self.player_mark)

    def cancel_marking(self):
        self.isPlayerMarking = False
        self.player_mark = None
        self.text_explanation = "Click on the field to mark player spots"

    "== REGISTER PLAYERS =="

    def create_player(self):
        if self.player_mark:
            if not self.isPlayerDirected:
                self.choose_player_direction()
            elif not self.isPlayerHasRole:
                self.choose_player_role()
            elif not self.isPlayerHasNumber:
                self.choose_player_number()
            
    
    def choose_player_direction(self):
        if self.player_mark:
            button_positions = {
                "left": (self.player_mark.x - 20 * 2 , self.player_mark.y + 10, 0),
                
                "top_left": (self.player_mark.x - 30, self.player_mark.topleft[1] - 30, 1),
                "top": (self.player_mark.x + 10, self.player_mark.y - 20 * 2, 2),
                "top_right": (self.player_mark.topright[0] + 10, self.player_mark.y - 30, 3),
                
                "right": (self.player_mark.right + 20, self.player_mark.y + 10, 4),
                
                "bottom_right": (self.player_mark.right + 10, self.player_mark.bottom +10, 5),
                "bottom": (self.player_mark.x + 10, self.player_mark.bottom + 20, 6),
                "bottom_left": (self.player_mark.x - 30, self.player_mark.bottom + 10, 7)
            }

            self.player_buttons = []
            for button_x, button_y, direction in button_positions.values():
                button = Button("", button_x, button_y, 20, 20, action=lambda d=direction: self.set_player_direction(d))
                self.player_buttons.append(button)
                button.draw(self.screen)

    def set_player_direction(self, direction):
        self.player_direction = direction
        self.isPlayerDirected = True

    def choose_player_role(self):
        self.text_explanation = "Choose the player role"
        
        button_roles = {
            "GK": (self.player_mark.x - 30, self.player_mark.bottom + 30),
            "DF": (self.player_mark.x + 10, self.player_mark.bottom + 30),
            "MD": (self.player_mark.right + 10, self.player_mark.bottom + 30),
            "FW": (self.player_mark.right + 50, self.player_mark.bottom + 30)
        }

        self.role_buttons = []
        for role, (button_x, button_y) in button_roles.items():
            button = Button(role, button_x, button_y, 35, 20, action=lambda r=role: self.set_player_role(r))
            self.role_buttons.append(button)
            button.draw(self.screen)
        
    def set_player_role(self, role):
        self.player_role = role
        self.isPlayerHasNumber = True
        self.choose_player_number()

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.cancel_marking()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.isPlayerMarking:
                        self.mark_player_spot(event.pos)
                
                if self.player_mark:
                    if self.player_mark and hasattr(self, 'player_buttons'):
                        for button in self.player_buttons:
                            button.is_clicked(event)
                    if self.player_mark and hasattr(self, 'role_buttons'):
                        for button in self.role_buttons:
                            button.is_clicked(event)

            self.update_title()

            self.draw_field()
            self.draw_player_spot() 
            self.create_player()

            pygame.display.update()