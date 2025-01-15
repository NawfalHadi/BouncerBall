import csv

from main.data.Player import Player

class Team():
    def __init__(self, id_team, name, nickname, color):
        self.id = id_team
        self.name = name
        self.nickname = nickname
        self.color = color

    def load_players(id_team):
        players = []
        with open('main/data/Player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['id_team']) == id_team:
                    player = Player(
                    id=int(row['id']),
                    name=row['name'],
                    number=int(row['number']),
                    role=row['role'],
                    id_team=int(row['id_team']),
                    x=float(row['x']),
                    y=float(row['y']),
                    direction=int(row['direction'])
                    )
                    players.append(player)
        return players