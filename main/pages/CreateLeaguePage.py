import pygame
import csv
import os

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

        "== INTERFACE =="
        self.text_explanation = "Press Up & Down Arrow To Change Team, \nPress Space to Put Teams In The League"

        "== TEMPORARY DATA =="
        self.league_teams = []

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

    "== CREATE LEAGUE =="
    def create_league(self):
        self.league_name = f"league_default"
        self.directory = 'main/db/leagues'
        
        # Check if the directory exists, if not, create it
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        
        file_path = os.path.join(self.directory, f'{self.league_name}.csv')
        
        # Check if the file exists, if not, create it
        if not os.path.isfile(file_path):
            with open(file_path, mode='w', newline='') as file:
                fieldnames = ['team_id', 'team_name', 'team_nickname', 'team_color', 'win', 'draw', 'lose', 'ga', 'gf', 'gd', 'point']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for team in self.league_teams:
                    writer.writerow({
                    'team_id': team.id,
                    'team_name': team.name,
                    'team_nickname': team.nickname,
                    'team_color': team.color,
                    'win': 0,
                    'draw': 0,
                    'lose': 0,
                    'ga': 0,
                    'gf': 0,
                    'gd': 0,
                    'point': 0
                    })

    def create_schedule(self):
        self.league_name = f"league_default"
        self.directory = 'main/db/leagues'
        schedule_directory = 'main/db/schedule'
        
        # Check if the directory exists, if not, create it
        if not os.path.exists(schedule_directory):
            os.makedirs(schedule_directory)
        
        schedule_file_path = os.path.join(schedule_directory, f'{self.league_name}.csv')
        
        # Generate the schedule
        schedule = []
        match_id = 1
        for i, home_team in enumerate(self.league_teams):
            for j, away_team in enumerate(self.league_teams):
                if home_team != away_team:
                    schedule.append({
                    'id': match_id,
                    'league_id': self.league_name,
                    'home_team_id': home_team.id,
                    'away_team_id': away_team.id,
                    'home_score': 0,
                    'away_score': 0,
                    'finish': False
                    })
                    match_id += 1
        
        # Write the schedule to the CSV file
        with open(schedule_file_path, mode='w', newline='') as file:
            fieldnames = ['id', 'league_id', 'home_team_id', 'away_team_id', 'home_score', 'away_score', 'finish']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for match in schedule:
                writer.writerow(match)

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

    def draw_input(self):
        keys = pygame.key.get_pressed()
        
        checkbox_rect = pygame.Rect(self.left_field.get_rect().left + 40, self.bottom_field.get_rect().top - 40, 20, 20)
        if self.current_team in self.league_teams:
            pygame.draw.rect(self.screen, BLACK, checkbox_rect)
            if keys[pygame.K_SPACE]:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.league_teams.remove(self.current_team)
        else:
            pygame.draw.rect(self.screen, BLACK, checkbox_rect, 2)
            if keys[pygame.K_SPACE]:
                pygame.time.wait(150)  # Add delay to slow down the key press
                self.league_teams.append(self.current_team)

        font = pygame.font.Font(None, 24)
        text_surface = font.render("Black means the teams joined the league", True, BLACK)
        text_rect = text_surface.get_rect(midleft=(checkbox_rect.right + 10, checkbox_rect.centery))
        self.screen.blit(text_surface, text_rect)

    def draw_instruction (self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text_explanation, True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, START_FIELD_HEIGHT - 50))
        self.screen.blit(text_surface, text_rect)

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
                    self.create_league()
                    self.create_schedule()
                    self.isRunning = False

            self.draw_field()

            self.draw_team()
            self.draw_player()
            self.draw_input()
            self.draw_instruction()
                    
            pygame.display.update()
            pygame.time.Clock().tick(60)
            