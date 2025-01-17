import pygame
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from constant.Size import *
from constant.Color import *
from ui.Button import Button

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        "== GAMEPLAY STATE =="
        self.isLoading = True
        self.isRunning = True

        self.init_interface()

    def init_interface(self):
        self.start_sim = Button("Start", 100, 100, 200, 100, action=self.start_simulation)
        self.create_teams = Button("Create Teams", 100, 250, 200, 100, action=self.create_teams_page)
        self.create_league = Button("Create League", 100, 400, 200, 100, action=self.create_league_page)
        self.show_league = Button("Show League", 100, 550, 200, 100, action=self.show_league_page)
    
    def draw_interface(self):
        self.start_sim.draw(self.screen)
        self.create_teams.draw(self.screen) 
        self.create_league.draw(self.screen)
        self.show_league.draw(self.screen)

    def start_simulation(self):
        from main.pages.GamesSimulationPage import GamesSimulationPage
        GamesSimulationPage().run()

    def create_teams_page(self):
        from main.pages.CreateTeamsPage import CreateTeamsPage
        CreateTeamsPage(5).run()

    def create_league_page(self):
        from main.pages.CreateLeaguePage import CreateLeaguePage
        CreateLeaguePage().run()

    def show_league_page(self):
        from main.pages.ShowLeaguePage import ShowLeaguePage
        ShowLeaguePage().run()

    def run(self):
        while self.isRunning:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                
                self.start_sim.is_clicked(event)
                self.create_teams.is_clicked(event)
                self.create_league.is_clicked(event)
                self.show_league.is_clicked(event)

            self.draw_interface()

            pygame.display.update()

if __name__ == "__main__":
    Main().run()
    pygame.quit()
    sys.exit()

