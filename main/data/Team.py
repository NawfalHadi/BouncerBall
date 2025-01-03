import csv

class Team():
    def __init__(self, id_team):
        self.db_path = "main/db/Team.db"
        self.load_teams(id_team)
    
    def load_teams(self, id_team):
        with open('main/data/teams.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) == id_team:
                    self.id = row['id']
                    self.name = row['name']
                    self.color = row['color']
                    self.nickname = row['nickname']
                    break

    def load_players(self):
        pass