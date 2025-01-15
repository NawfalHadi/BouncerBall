import pygame
import csv

from main.constant.Size import *
from main.constant.Color import *

from main.ui.Line import Line
from main.ui.TextBox import TextBox

from main.data.Team import Team
from main.data.Player import Player

class CreateLeaguePage:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        "== DATA =="
        self.teams_list = self.load_teams()
        self.player_list = None

        "== CURSOR STATE =="
        self.cursor_index = 4
        self.current_team = self.teams_list[self.cursor_index]

        self.init_field()
        self.load_player(int(self.current_team.id))

    "== FIELD =="

    def init_field(self):
        self.left_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)
        self.top_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT), BLACK)
        self.bottom_field = Line((START_FIELD_WIDHT, START_FIELD_HEIGHT + FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.center_field = Line((START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH // 2, START_FIELD_HEIGHT + FIELD_HEIGHT), BLACK)

        self.top_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT), BLACK)
        self.bottom_gk_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)
        self.gk_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_GK_WIDHT, START_FIELD_GK_HEIGHT + FIELD_GK_HEIGHT), BLACK)

        self.top_df_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_DF_HEIGHT), BLACK)
        self.bottom_df_right_field = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)
        self.df_right_vertical = Line((START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT), (START_FIELD_WIDHT + FIELD_WIDTH - FIELD_DF_WIDHT, START_FIELD_DF_HEIGHT + FIELD_DF_HEIGHT), BLACK)
    
    def draw_field(self):
        self.left_field.draw(self.screen)
        self.right_field.draw(self.screen)
        self.top_field.draw(self.screen)
        self.bottom_field.draw(self.screen)


        self.center_field.draw(self.screen)
        self.center_circle = pygame.draw.circle(self.screen, BLACK, (START_FIELD_WIDHT + FIELD_WIDTH / 2, START_FIELD_HEIGHT + FIELD_HEIGHT / 2), 73, 2)
        
        self.top_gk_right_field.draw(self.screen)
        self.bottom_gk_right_field.draw(self.screen)
        self.gk_right_vertical.draw(self.screen)

        self.top_df_right_field.draw(self.screen)
        self.bottom_df_right_field.draw(self.screen)
        self.df_right_vertical.draw(self.screen)

    "== DATA =="

    def load_teams(self):
        teams = []
        with open('main/db/Teams.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                team = Team(
                    id_team=row['id'],
                    name=row['name'],
                    nickname=row['nickname'],
                    color=row['color']
                    )
                teams.append(team)
        return teams

    def load_player(self, id_team):
        players = []
        with open('main/db/Player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['id_team']) == id_team:
                    player = Player(
                    name=row['name'],
                    x=float(row['x']),
                    y=float(row['y']),
                    width=35,
                    height=35,
                    color=self.current_team.color,
                    role=row['role'],
                    side="R",
                    number=int(row['number']),
                    path=int(row['direction'])
                    )

                    player.set_position()
                    players.append(player)
        
        self.player_list = players

    "== CHOOSE TEAM =="

    def update_current_team(self):
        self.current_team = self.teams_list[self.cursor_index] 

    "== INTERFACE =="

    def draw_team(self):
        team_name_text = TextBox(
            f"{self.current_team.name} : {self.current_team.id}" ,
            self.left_field.get_rect().left + 150,
            self.center_circle.centery - 100,
            300, 50, self.current_team.color
            ).draw(self.screen)

        team_rectangle = TextBox(
            self.current_team.nickname,
            self.left_field.get_rect().left + 150,
            self.center_circle.centery - 0,
            300, 100, self.current_team.color 
            ).draw(self.screen)

    
    def draw_player(self):
        for player in self.player_list:
            player.draw(self.screen)
            player.get_names(self.screen)
        
    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_UP]:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index = (self.cursor_index - 1) % len(self.teams_list)
                self.update_current_team()
                self.load_player(int(self.current_team.id))
            elif keys[pygame.K_DOWN]:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.cursor_index = (self.cursor_index + 1) % len(self.teams_list)
                self.update_current_team()
                self.load_player(int(self.current_team.id))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw_field()
            self.draw_team()
            self.draw_player()
                    
            pygame.display.update()
            pygame.time.Clock().tick(60)
            