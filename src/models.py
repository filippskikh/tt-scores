import json


class Team:
    id: str = None
    name: str = None

    def to_dict(self):
        return self.__dict__


def team_from_dict(d):
    team = Team()
    team.id = d['id']
    team.name = d['name']

    return team


class Game:
    id: str = None
    score1: int = 0
    score2: int = 0
    team1_id: str = None
    team2_id: str = None
    timestamp: int = 0

    def to_dict(self):
        return self.__dict__


def game_from_dict(d):
    game = Game()
    game.id = d['id']
    game.score1 = int(d['score1'])
    game.score2 = int(d['score2'])
    game.team1_id = d['team1_id']
    game.team2_id = d['team2_id']
    game.timestamp = d['timestamp']

    return game
