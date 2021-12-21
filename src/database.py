import time
import uuid
import models
import requests

GAMES_INDEX = "games"
TEAMS_INDEX = "teams"
ELASTIC_ADDRESS = "http://elastic:9200"


def get_games():
    body = {
        "size": 10000,
        "query": {
            "match_all": {}
        }
    }

    response = requests.post(ELASTIC_ADDRESS + "/" + GAMES_INDEX + "/_search", json=body).json()
    print(response)

    games = []
    for hit in response['hits']['hits']:
        games.append(models.game_from_dict(hit['_source']))

    return games


def add_game(team1_id, score1, team2_id, score2):
    game = models.Game()
    game.team1_id = team1_id
    game.team2_id = team2_id
    game.score1 = int(score1)
    game.score2 = int(score2)
    game.id = str(uuid.uuid4())
    game.timestamp = int(round(time.time() * 1000))

    response = requests.post(ELASTIC_ADDRESS + "/" + GAMES_INDEX + "/_doc/" + game.id + "?refresh=true", json=game.to_dict()).json()
    print(response)


def get_teams():
    body = {
        "size": 10000,
        "query": {
            "match_all": {}
        }
    }

    response = requests.post(ELASTIC_ADDRESS + "/" + TEAMS_INDEX + "/_search", json=body).json()
    print(response)

    teams = []
    for hit in response['hits']['hits']:
        teams.append(models.team_from_dict(hit['_source']))

    return teams


def add_team(team_name):
    team = models.Team()
    team.name = team_name
    team.id = str(uuid.uuid4())

    response = requests.post(ELASTIC_ADDRESS + "/" + TEAMS_INDEX + "/_doc/" + team.id + "?refresh=true", json=team.to_dict()).json()
    print(response)


def init():
    requests.put(ELASTIC_ADDRESS + "/" + GAMES_INDEX)
    requests.put(ELASTIC_ADDRESS + "/" + TEAMS_INDEX)