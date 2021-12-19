from datetime import datetime

from typing import List

import models


class Team:
    id: str = None
    name: str = None
    wins: int = 0
    losses: int = 0
    draws: int = 0


class Game:
    score1: int = 0
    score2: int = 0
    team1_name: str = None
    team2_name: str = None
    date: str = None


def convert_to_view_model(teams: List[models.Team], games: List[models.Game]):
    view_teams = {}
    for team in teams:
        view_team = Team()
        view_team.name = team.name
        view_team.id = team.id
        view_teams[team.id] = view_team

    view_games = []
    for game in games:
        view_game = Game()
        view_game.score1 = game.score1
        view_game.score2 = game.score2
        view_game.date = datetime.utcfromtimestamp(int(game.timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')

        view_game.team1_name = view_teams[game.team1_id].name
        view_game.team2_name = view_teams[game.team2_id].name

        if view_game.score1 == view_game.score2:
            view_teams[game.team1_id].draws += 1
            view_teams[game.team2_id].draws += 1
        elif view_game.score1 > view_game.score2:
            view_teams[game.team1_id].wins += 1
            view_teams[game.team2_id].losses += 1
        else:
            view_teams[game.team1_id].losses += 1
            view_teams[game.team2_id].wins += 1

        view_games.append(view_game)

    return view_teams.values(), view_games
