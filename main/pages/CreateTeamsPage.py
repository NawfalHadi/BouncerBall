import pygame
import csv

from main.constant.Size import *
from main.constant.Color import *

from main.ui.Line import Line
from main.ui.Button import Button
from main.ui.InputText import InputText

from main.data.Player import Player

class CreateTeamsPage:
    def __init__(self, team_id):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Create Teams")

        "== PAGE STATE =="
        self.isLoading = True
        self.isRunning = True

        "== PLAYER =="
        self.id_team = team_id
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
        self.init_button()

    "== INTERFACE =="
    def update_title(self):
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text_explanation, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=(SCREEN_WIDTH // 2, START_FIELD_HEIGHT - 50))
        self.screen.blit(self.text_surface, self.text_rect)

    def init_button(self):
        self.save_csv = Button("Submit Team", (SCREEN_WIDTH // 2) - 100, SCREEN_HEIGHT - 125, 200, 50, BLACK, RED, action=self.save_players_to_csv)
    
    def draw_button(self):
        self.save_csv.draw(self.screen)

    "== FIELD =="

    def init_field(self):
        self.left_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.top_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), BLACK)
        self.bottom_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_left_field = Line((START_FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_GK_WIDHT + FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_left_field = Line((START_FIELD_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_left_vertical = Line((START_FIELD_WIDHT + FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

        self.top_df_left_field = Line((START_FIELD_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_DF_WIDHT + FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), BLACK)
        self.bottom_df_left_field = Line((START_FIELD_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)
        self.df_left_vertical = Line((START_FIELD_WIDHT + FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)

        self.center_field = Line((START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT), RED)
        self.bottom_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), RED)
        self.gk_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

        self.top_df_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_DF_HEIGHT), BLACK)
        self.bottom_df_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)
        self.df_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)

    def draw_field(self):
        self.left_field.draw(self.screen)
        self.right_field.draw(self.screen)
        self.top_field.draw(self.screen)
        self.bottom_field.draw(self.screen)

        self.top_gk_left_field.draw(self.screen)
        self.bottom_gk_left_field.draw(self.screen)
        self.gk_left_vertical.draw(self.screen)

        self.top_df_left_field.draw(self.screen)
        self.bottom_df_left_field.draw(self.screen)
        self.df_left_vertical.draw(self.screen)

        self.center_field.draw(self.screen)
        self.center_circle = pygame.draw.circle(self.screen, BLACK, (START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2), 73, 2)

        self.top_gk_right_field.draw(self.screen)
        self.bottom_gk_right_field.draw(self.screen)
        self.gk_right_vertical.draw(self.screen)

        self.top_df_right_field.draw(self.screen)
        self.bottom_df_right_field.draw(self.screen)
        self.df_right_vertical.draw(self.screen)

    "== MARKING =="
    def mark_player_spot(self, pos):
        x, y = pos
        if START_FIELD_WIDHT <= x <= START_FIELD_WIDHT + (FIELD_WIDTH / 2)  and START_FIELD_HEIGHT <= y <= START_FIELD_HEIGHT + FIELD_HEIGHT:
            self.text_explanation = "Choose the player direction when games start \nEsc to cancel"
            self.player_mark = pygame.Rect(x - 25, y - 25, 40, 40)
            self.isPlayerMarking = True

            # Initiate the input text
            self.init_input_player_number()
            self.init_input_player_name()

    def draw_player_spot(self):
        if self.player_mark:
            pygame.draw.rect(self.screen, RED, self.player_mark)

    def cancel_marking(self):
        self.isPlayerMarking = False
        self.player_mark = None
        self.text_explanation = "Click on the left area of the field to mark player spots"

        self.isPlayerDirected = False
        self.isPlayerHasName = False
        self.isPlayerHasNumber = False
        self.isPlayerHasRole = False
        
        self.player_name = None
        self.player_number = 0
        self.player_role = None
        self.player_direction = 0
        
        try:
            self.input_player_name.isActive = False
            self.input_player_number.isActive = False
        except Exception as e:
            pass

    "== REGISTER PLAYERS =="

    def create_player(self):
        if self.player_mark:
            if not self.isPlayerDirected:
                self.choose_player_direction()
            elif not self.isPlayerHasRole:
                self.choose_player_role()
            elif not self.isPlayerHasNumber:
                self.choose_player_number()
            elif not self.isPlayerHasName:
                self.choose_player_name()
            
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
        self.text_explanation = "Choose the player role"

        self.player_direction = direction
        self.isPlayerDirected = True

    def choose_player_role(self):        
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
        if self.player_position_available():
            self.isPlayerHasRole = True
            self.text_explanation = "Type your player number, then press Enter"

    
    def init_input_player_number(self):
        self.input_player_number = InputText(self.player_mark.centerx - 20, self.player_mark.bottom + 20, 40, 40, GRAY, GREEN, 2)
        self.input_player_number.isActive = True

    def choose_player_number(self):
        self.input_player_number.draw(self.screen)
        self.input_player_number.activate_input()
        self.input_player_number.check_input()

    def set_player_number(self):
        self.player_number = self.input_player_number.text
        
        if len(self.player_number) > 0 and self.player_number.isdigit():
            if self.player_number_available():
                self.isPlayerHasNumber = True
                self.input_player_number.isActive = False
                
                self.input_player_name.isActive = True
                self.text_explanation = "Type your player name, then press Enter"
        elif len(self.player_number) == 0:
            self.text_explanation = "Dont empty the player number"
        elif not self.player_number.isdigit():
            self.text_explanation = "Player number must be a number"

    def typing_player_number(self, event):
        if self.input_player_number.isActive:
            if event.key == pygame.K_RETURN:
                self.set_player_number()
            elif event.key == pygame.K_BACKSPACE:
                self.input_player_number.text = self.input_player_number.text[:-1]
            else:
                if self.isPlayerHasRole:
                    self.input_player_number.text += event.unicode
                    self.input_player_number.draw(self.screen)

        elif not self.input_player_number.isActive and not self.isPlayerHasNumber:
            if event.key == pygame.K_RETURN:
                self.set_player_number()
            elif event.key == pygame.K_BACKSPACE:
                self.input_player_number.text = self.input_player_number.text[:-1]

    def init_input_player_name(self):
        self.input_player_name = InputText(self.player_mark.centerx - 100, self.player_mark.bottom + 20, 200, 40, GRAY, GREEN, 100)

    def choose_player_name(self):

        self.input_player_name.draw(self.screen)
        self.input_player_name.activate_input()
        self.input_player_name.check_input()

    def set_player_name(self):
        if len(self.input_player_name.text) > 0:
            if self.player_spot_available():
                self.player_name = self.input_player_name.text
                self.isPlayerHasName = True
                self.input_player_name.isActive = False
            
                self.player_saved()
                
    def typing_player_name(self, event):
        if self.input_player_name.isActive:
            if event.key == pygame.K_RETURN:
                self.set_player_name()
            elif event.key == pygame.K_BACKSPACE:
                self.input_player_name.text = self.input_player_name.text[:-1]
            else:
                self.input_player_name.text += event.unicode
                self.input_player_name.draw(self.screen)

        elif not self.input_player_name.isActive:
            if event.key == pygame.K_RETURN:
                self.set_player_name()
            elif event.key == pygame.K_BACKSPACE:
                self.input_player_name.text = self.input_player_name.text[:-1]

    def player_saved(self):
        if self.isPlayerHasName and self.isPlayerHasNumber and self.isPlayerHasRole:
            player = {
                "name": self.player_name,
                "number": self.player_number,
                "role": self.player_role,
                "direction": self.player_direction,
                "position": (self.player_mark.center[0] - START_FIELD_WIDHT, self.player_mark.center[1] - START_FIELD_HEIGHT),
                "id_team": self.id_team
            }

            self.players.append(player)
            

            self.player_mark = None
            self.isPlayerMarking = False
            self.isPlayerDirected = False
            self.isPlayerHasRole = False
            self.isPlayerHasNumber = False
            self.isPlayerHasName = False
    
    "== SHOW PLAYERS =="

    def show_players(self):
        if len(self.players) > 0:
            for player in self.players:
                player = Player(player["name"], player["position"][0], player["position"][1], 40, 40, RED, player["role"], "L", player["number"])
                player.set_position()
                player.draw(self.screen)
                player.get_names(self.screen)


    "== DELETE PLAYERS =="

    "== SUBMIT VALIDATION =="

    def player_spot_available(self):
        if len(self.players) == 11:
            self.text_explanation = "You have reached the maximum player, press Esc to cancel"
            return False        
        
        return True

    def player_number_available(self):
        if self.player_number in [player["number"] for player in self.players]:
            self.text_explanation = "This player number is already taken, press Esc to cancel"
            return False

        return True
    
    def player_position_available(self):
        gk_count = sum(1 for player in self.players if player["role"] == "GK")
        df_count = sum(1 for player in self.players if player["role"] == "DF")
        md_count = sum(1 for player in self.players if player["role"] == "MD")
        fw_count = sum(1 for player in self.players if player["role"] == "FW")

        print(gk_count, df_count, md_count, fw_count)
        
        if self.player_role == "GK":
            print("GK")
            if gk_count == 1:
                self.text_explanation = "You have reached the maximum (1) goalkeeper, press Esc to cancel"
                return False
        if self.player_role == "DF":
            print("DF")
            if df_count == 5:
                self.text_explanation = "You have reached the maximum (5) defender, press Esc to cancel"
                return False
        if self.player_role == "MD":
            print("MD")
            if md_count == 5:
                self.text_explanation = "You have reached the maximum (5) midfielder, press Esc to cancel"
                return False
        if self.player_role == "FW":
            print("FW")
            if fw_count == 3:
                self.text_explanation = "You have reached the maximum (3) forward, press Esc to cancel"
                return False
        
        print(gk_count, df_count, md_count, fw_count)
        
        return True

    "== STORAGE =="

    def save_players_to_csv(self, filename="main/db/Player.csv"):
        if len(self.players) < 11:
            self.text_explanation = "You need to fill 11 players"
        else:
            try:
                with open(filename, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    existing_players = list(reader)
                    next_id = len(existing_players)  # Calculate the next id based on existing players
            except FileNotFoundError:
                next_id = 1  # If file does not exist, start with id 1

            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                if next_id == 1:
                    writer.writerow(["id", "name", "number", "role", "id_team", "x", "y", "direction"])
                for player in self.players:
                    writer.writerow([
                        next_id,
                        player["name"],
                        player["number"],
                        player["role"],
                        player["id_team"],
                        player["position"][0],
                        player["position"][1],
                        player["direction"]
                    ])
                    next_id += 1

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.cancel_marking()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.isPlayerMarking:
                        self.mark_player_spot(event.pos)

                "== INPUT PLAYER NUMBER =="

                if event.type == pygame.KEYDOWN:
                    try:
                        self.typing_player_number(event)
                        self.typing_player_name(event)
                    except Exception as e:
                        pass
                "========================"

                if self.player_mark:
                    if self.player_mark and hasattr(self, 'player_buttons'):
                        for button in self.player_buttons:
                            button.is_clicked(event)
                    if self.player_mark and hasattr(self, 'role_buttons'):
                        for button in self.role_buttons:
                            button.is_clicked(event)

                self.save_csv.is_clicked(event)

            self.update_title()

            self.draw_field()
            self.draw_player_spot() 
            self.create_player()

            self.show_players()
            self.draw_button()

            pygame.display.update()